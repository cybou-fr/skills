from __future__ import annotations
import re
from typing import Dict, List

IP_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
DOMAIN_RE = re.compile(r"\b(?:[a-zA-Z0-9-]{1,63}\.)+(?:com|net|org|io|dev|fr|ru|co|cloud|internal)\b")
URL_RE = re.compile(r"https?://[^\s\"'<>]+")
SHA256_RE = re.compile(r"\b[a-fA-F0-9]{64}\b")
SHA1_RE = re.compile(r"\b[a-fA-F0-9]{40}\b")
MD5_RE = re.compile(r"\b[a-fA-F0-9]{32}\b")
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
AWS_ARN_RE = re.compile(r"arn:aws:[A-Za-z0-9_:/.-]+")

def unique(xs):
    return sorted(set(x.rstrip('.,;:') for x in xs if x))

def extract_iocs(text: str) -> Dict[str, List[str]]:
    urls = unique(URL_RE.findall(text))
    return {
        'ips': unique(IP_RE.findall(text)),
        'domains': unique([d for d in DOMAIN_RE.findall(text) if not any(d in u for u in urls)]),
        'urls': urls,
        'sha256': unique(SHA256_RE.findall(text)),
        'sha1': unique(SHA1_RE.findall(text)),
        'md5': unique(MD5_RE.findall(text)),
        'emails': unique(EMAIL_RE.findall(text)),
        'aws_arns': unique(AWS_ARN_RE.findall(text)),
    }

def summarize_iocs(text: str) -> Dict:
    iocs = extract_iocs(text)
    count = sum(len(v) for v in iocs.values())
    return {'ioc_count': count, 'iocs': iocs}
