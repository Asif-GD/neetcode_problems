def num_unique_emails(emails: list[str]) -> int:
    hashset = set()

    for email_item in emails:
        # using split() but it excludes the "@"; will add it later in the end using join()
        # although partition() includes the "@", I didn't use it because it returns a tuple, and they are unmodifiable
        # didn't want the extra step of converting the tuple to a list.
        split_email_string = email_item.split("@")
        # print(f"split_email_string = {split_email_string}")

        no_of_plus = split_email_string[0].count("+")
        # print(f"no_of_plus = {no_of_plus}")
        # rule 1: search for "+" in the local name part and ignore it and everything after it.
        if no_of_plus:
            # print("inside if 1")
            plus_position = split_email_string[0].find("+")
            split_email_string[0] = split_email_string[0][:plus_position]
            # print(f"split_email_string[0] = {split_email_string[0]}")

        no_of_dots = split_email_string[0].count(".")
        # print(f"no_of_dots = {no_of_dots}")
        # rule 2: search for "." in the local name part and remove it.
        if no_of_dots:
            # print("inside if 2")
            split_email_string[0] = split_email_string[0].replace(".", "", no_of_dots)
            # print(f"split_email_string[0] = {split_email_string[0]}")

        formatted_email = "@".join(split_email_string)
        # print(f"formatted_email = {formatted_email}")
        # set() allows only unique elements, so no duplicates. len(hashset) = number of unique mail addresses.
        hashset.add(formatted_email)

    return len(hashset)


print(num_unique_emails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(num_unique_emails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
