;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	security.utwente.nl. root.localhost. (
			      2		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
; NS Records
@	IN	NS	localhost.

; A Records
@	IN	A	127.0.0.1

gamer-book-hammer IN A 127.0.0.1
gamer-book-hammer IN TXT "123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 1234"
gamer-book-hammer IN MX 10 mail10-XhVgXRzrpkRgL9cW2qNm.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 11 mail11-mEy6Hbwxzyt9XMEs2PKL.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 12 mail12-rzyAq2VjxhfwjyXPr5QY.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 13 mail13-8LeUU8CsDQL837mLPtMt.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 14 mail14-NrLKpN8vw63hSrHjq5Gk.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 15 mail15-qYJXMyY8Utrc3QUD9pXt.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 20 mail20-XhVgXRzrpkRgL9cW2qNm.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 21 mail21-mEy6Hbwxzyt9XMEs2PKL.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 22 mail22-rzyAq2VjxhfwjyXPr5QY.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 23 mail23-8LeUU8CsDQL837mLPtMt.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 24 mail24-NrLKpN8vw63hSrHjq5Gk.gamer-book-hammer.security.utwente.nl
gamer-book-hammer IN MX 25 mail25-qYJXMyY8Utrc3QUD9pXt.gamer-book-hammer.security.utwente.nl

@	IN	AAAA	::1
