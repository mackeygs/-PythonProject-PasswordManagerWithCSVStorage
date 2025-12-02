import csv
import argparse
import os
import re
import random
import string

CSV_FILE = "passwords.csv"

# ----------------------------
# Helper functions
# ----------------------------

def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["site", "username", "password"])


def read_csv():
    ensure_csv()
    with open(CSV_FILE, "r") as f:
        return list(csv.DictReader(f))


def write_csv(rows):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["site", "username", "password"])
        writer.writeheader()
        writer.writerows(rows)


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


# Regex to validate site names (simple domain pattern)
SITE_REGEX = re.compile(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$")

# ----------------------------
# Actions
# ----------------------------

def add_entry(site, username, password):
    if not SITE_REGEX.match(site):
        raise ValueError("Invalid site format. Example: example.com")

    rows = read_csv()
    for r in rows:
        if r["site"] == site:
            raise ValueError("Site already exists.")

    rows.append({"site": site, "username": username, "password": password})
    write_csv(rows)
    print(f"Added credentials for {site}")


def get_entry(site):
    rows = read_csv()
    for r in rows:
        if r["site"] == site:
            print(f"Site: {r['site']}\nUser: {r['username']}\nPass: {r['password']}")
            return
    print("No entry found.")


def update_entry(site, field, value):
    if field not in ["username", "password"]:
        raise ValueError("Field must be 'username' or 'password'")

    rows = read_csv()
    found = False

    for r in rows:
        if r["site"] == site:
            r[field] = value
            found = True

    if not found:
        print("Site not found.")
    else:
        write_csv(rows)
        print(f"Updated {field} for {site}")


def delete_entry(site):
    rows = read_csv()
    new_rows = [r for r in rows if r["site"] != site]

    if len(rows) == len(new_rows):
        print("Site not found.")
    else:
        write_csv(new_rows)
        print(f"Deleted entry for {site}")


def generate_and_store(site, username, length):
    password = generate_password(length)
    add_entry(site, username, password)
    print(f"Generated password: {password}")


# ----------------------------
# Argument Parsing
# ----------------------------

def main():
    parser = argparse.ArgumentParser(description="Password Manager with CSV Storage")

    parser.add_argument("-add", nargs=3, metavar=("SITE", "USER", "PASS"))
    parser.add_argument("-get", nargs=1)
    parser.add_argument("-update", nargs=3, metavar=("SITE", "FIELD", "VALUE"))
    parser.add_argument("-delete", nargs=1)
    parser.add_argument("-gen", nargs=3, metavar=("SITE", "USER", "LENGTH"))

    args = parser.parse_args()

    try:
        if args.get is not None:
            get_entry(args.get[0])

        elif args.add is not None:
            site, user, pw = args.add
            add_entry(site, user, pw)

        elif args.update is not None:
            site, field, value = args.update
            update_entry(site, field, value)

        elif args.delete is not None:
            delete_entry(args.delete[0])

        elif args.gen is not None:
            site, user, length_str = args.gen
            if not length_str.isdigit():
                raise ValueError("Password length must be a number")
            generate_and_store(site, user, int(length_str))

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
