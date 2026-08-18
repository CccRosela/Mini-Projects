import re

def main():
    print(validate(input("IP Address: ").strip()))

def validate(ip):
    pattern = r"(\d{1,3}\.){3}(\d{1,3})"
    try:
        if re.fullmatch(pattern, ip):
            for part in (ip.split(".")):
                if int(part) > 255:
                    raise ValueError
                
                if ip == "0.0.0.0":
                    return "Valid IP. (Warning: Non-routable/Unspecified address)"
            
            return "Valid IP address! :D"
        else:
            return "Invalid IP address."
    except ValueError:
        return f"Invalid IP address: 0 < Digits ≤ 255"


if __name__ == "__main__":
    main()
