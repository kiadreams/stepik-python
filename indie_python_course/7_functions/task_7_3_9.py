def get_domain_name(url):
    prf = ["https://", "www."]
    domain_name = url.removeprefix("http://")
    for p in prf:
        domain_name = domain_name.removeprefix(p)
    return domain_name.split(".")[0]


get_domain_name("http://google.com")
