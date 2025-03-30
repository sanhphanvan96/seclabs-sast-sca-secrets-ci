import json
from collections import Counter, defaultdict
from argparse import ArgumentParser


def sarif_to_markdown(
    sarif_file_path,
    output_file_path=None,
    repo_url=None,
    branch="main",
    title="Static Analysis Report",
    use_table=False,
    use_icons=True,
):
    # Severity icons
    severity_emojis = (
        {"Error": "🔥", "Warning": "⚠️", "Note": "ℹ️"}
        if use_icons
        else {"Error": "", "Warning": "", "Note": ""}
    )
    severity_order = {"Error": 3, "Warning": 2, "Note": 1}  # For sorting in table mode

    # Read the SARIF file
    with open(sarif_file_path, "r", encoding="utf-8") as f:
        sarif_data = json.load(f)

    # Initialize Markdown string
    markdown = f"# {title}\n\n"

    # Extract results from SARIF
    results = sarif_data.get("runs", [{}])[0].get("results", [])
    if not results:
        markdown += "No issues found.\n"
        return markdown

    # Count issues by severity, including zeros
    severity_counts = Counter(
        result.get("level", "note").capitalize() for result in results
    )
    total_issues = len(results)
    all_severities = ["Error", "Warning", "Note"]
    severity_summary = ", ".join(
        f"{severity_counts.get(level, 0)} {severity_emojis.get(level, '')} {level}{'s' if severity_counts.get(level, 0) != 1 else ''}"
        for level in all_severities
    )
    markdown += f"Total: **{total_issues}** issues detected ({severity_summary}).\n\n"

    # Helper function to format an issue
    def format_issue(i, result):
        rule_id = result.get("ruleId", "N/A")
        message = result.get("message", {}).get("text", "No description available")
        level = result.get("level", "note").capitalize()
        location = result.get("locations", [{}])[0].get("physicalLocation", {})
        file_path = location.get("artifactLocation", {}).get("uri", "N/A")
        region = location.get("region", {})
        start_line = region.get("startLine", "N/A")
        location_link = (
            f"[{file_path}#L{start_line}]({repo_url}/blob/{branch}/{file_path}#L{start_line})"
            if repo_url
            else f"{file_path}:{start_line}"
        )
        return rule_id, message, level, location_link

    if use_table:
        # Table format: sort by severity (Error > Warning > Note)
        markdown += "## Issue Details\n\n"
        markdown += "<details>\n<summary>Click to view details</summary>\n\n"
        markdown += "| # | Rule ID | Severity | Description | Location |\n"
        markdown += "|---|---------|----------|-------------|----------|\n"
        sorted_results = sorted(
            results,
            key=lambda r: severity_order.get(r.get("level", "note").capitalize(), 0),
            reverse=True,
        )
        for i, result in enumerate(sorted_results, 1):
            rule_id, message, level, location_link = format_issue(i, result)
            emoji = severity_emojis.get(level, "")
            markdown += (
                f"| {i} | {rule_id} | {emoji} {level} | {message} | {location_link} |\n"
            )
        markdown += "\n</details>\n"
    else:
        # Normal format: separate sections by severity
        issues_by_severity = defaultdict(list)
        for result in results:
            level = result.get("level", "note").capitalize()
            issues_by_severity[level].append(result)

        for level in ["Error", "Warning", "Note"]:
            if issues_by_severity[level]:
                count = len(issues_by_severity[level])
                emoji = severity_emojis.get(level, "")
                markdown += f"## {emoji} {level}s\n"
                markdown += f"<details>\n<summary>{count} {level}{'s' if count > 1 else ''}</summary>\n\n"
                for i, result in enumerate(issues_by_severity[level], 1):
                    rule_id, message, level, location_link = format_issue(i, result)
                    markdown += f"### Issue {i}: {rule_id}\n"
                    markdown += f"- **Severity**: {emoji} {level}\n"
                    markdown += f"- **Description**: {message}\n"
                    markdown += f"- **Location**: {location_link}\n\n"
                markdown += "</details>\n\n"

    # Write to file if output path is provided
    if output_file_path:
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(markdown)
    return markdown


# Command-line interface
if __name__ == "__main__":
    parser = ArgumentParser(description="Convert SARIF to Markdown")
    parser.add_argument("sarif_file", help="Path to the SARIF file")
    parser.add_argument(
        "--output", help="Path to the output Markdown file", default="output.md"
    )
    parser.add_argument(
        "--repo-url", help="Repository URL for linking locations", default=None
    )
    parser.add_argument("--branch", help="Branch name for repo links", default="main")
    parser.add_argument(
        "--title", help="Custom title for the report", default="Static Analysis Report"
    )
    parser.add_argument(
        "--table", action="store_true", help="Use table format instead of normal format"
    )
    parser.add_argument(
        "--no-icons", action="store_true", help="Disable severity icons"
    )
    args = parser.parse_args()

    markdown_output = sarif_to_markdown(
        sarif_file_path=args.sarif_file,
        output_file_path=args.output,
        repo_url=args.repo_url,
        branch=args.branch,
        title=args.title,
        use_table=args.table,
        use_icons=not args.no_icons,
    )
    print(markdown_output)
