import csv
from github import Github
from datetime import datetime, timezone

g = Github("")

repo_owner = 'nodejs'
repo_name = 'node'

repo = g.get_repo(f"{repo_owner}/{repo_name}")

start_date = datetime(2023, 1, 1, tzinfo=timezone.utc)
end_date = datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc)

open_prs = repo.get_pulls(state='open')
closed_prs = repo.get_pulls(state='closed')

csv_file_name = "Raw_Data.csv"

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["Title", "Created At", "Updated At", "Additions", "Commits", "Status", "Comments", "Merged At", "Author"])

    for pr in open_prs:
        if start_date <= pr.created_at <= end_date:
            writer.writerow(
                [pr.title, pr.created_at, pr.updated_at, pr.additions, pr.commits, "Open", pr.comments, "", pr.user.login])

    for pr in closed_prs:
        if start_date <= pr.created_at <= end_date:
            status = "Closed"
            merged_at = ""
            if pr.merged:
                status = "Merged"
                merged_at = pr.merged_at
            writer.writerow(
                [pr.title, pr.created_at, pr.updated_at, pr.additions, pr.commits, status, pr.comments, merged_at, pr.user.login])

print("Data has been written to the CSV file successfully.")
