## Project To Demontrate Django skill

### Prerequisites

What things you need to install the software and how to install them

```
python 2.7 or 3.5
Django
```



### Sample Code

What things you need to install the software and how to install them

```python
def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)

		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['trevelynjune@gmail.com'])
			except BadHeaderError:
				return HttpResponse('invalid header found.')
			return redirect('success')
	return render(request,'contact.html', {'form' : form})

def team(request):
	return render(request, 'team.html')
```


## Final output
