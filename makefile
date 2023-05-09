# command is make git m="message"
git:
	git add .
	git commit -m "$m"
	git push -u origin main
