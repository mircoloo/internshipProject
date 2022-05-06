domain_match = re.search(domain_re, text.replace('\n', ''))
            if(domain_match):
                print(domain_match.group(1))
