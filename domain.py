from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

def get_project_name(url):
    try:
        project_name = get_sub_domain_name(url).split('.')
        return project_name[-2] + '-' + project_name[-1]
    except:
        return ''