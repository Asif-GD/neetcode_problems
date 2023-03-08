def num_unique_emails(emails: list[str]) -> int:
    unique_emails = set()

    for email_item in emails:
        i, local_name = 0, ""

        # adding all char to local_name if they aren't @ or +
        while email_item[i] not in ["@", "+"]:
            if email_item[i] != ".":
                local_name += email_item[i]
            i += 1

        # adding all char from @ to end to domain_name
        while email_item[i] != "@":
            i += 1
        domain_name = email_item[i:]

        unique_emails.add(local_name + domain_name)

    # print(unique_emails)
    return len(unique_emails)


print(num_unique_emails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(num_unique_emails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
