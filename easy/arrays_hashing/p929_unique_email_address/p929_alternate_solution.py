def num_unique_emails(emails: list[str]) -> int:
    unique_emails = set()

    for email_item in emails:
        # splitting the local and domain parts
        local_name, domain_name = email_item.split("@")

        # 1 - ignoring everything after +, inclusive.
        local_name = local_name.split("+")[0]

        # 2 - removing dots.
        local_name = local_name.replace(".", "")

        email_item = local_name + "@" + domain_name
        unique_emails.add(email_item)

    return len(unique_emails)


print(num_unique_emails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(num_unique_emails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
