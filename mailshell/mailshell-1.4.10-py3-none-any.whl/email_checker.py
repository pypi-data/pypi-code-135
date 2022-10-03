import sys, os
import imaplib, email
import html_text, base64
from datetime import datetime
from email.header import decode_header

DATE = datetime.now().strftime('%d-%b-%Y')
PARTS = "(RFC822)"
IMAP_SERVER = "imap.gmail.com"
LINE = f"\x1b[33m{'-' * 55}\x1b[0m"

def mailbox_error(box):
	print(f"\nERROR: [{box}]: mailbox does not exist!. Use 'msl check -lb' to see your mailboxes.\n")

def criteria_error(cri):	
	print("\nERROR: No search command: you didn't add a selector. Use 'msl ckeck -h' to see the selection commands.\n")

def decode_message(string):
	try: string = base64.b64decode(string.encode("utf8")).decode("utf8")
	except: pass
	part = decode_header(html_text.extract_text(string))[0]
	if not part[1]: return part[0]
	part = part[0].decode(part[1])
	return part

def select_mailbox(client, box):
	if not box or box == "Inbox": return "Inbox"
	for mb in client.list()[1]:
		mb = mb.decode().split(' "/" ')
		if box.title() in mb[1]:
			return mb[1]
	return

def generate_criteria(args):
	cri = ""
	if args.all: cri += 'ALL'
	if args.new and args.date: cri += f'SINCE {args.date}'
	else:
		if args.new: cri += f'ON {DATE}'
		if args.date: cri += f'ON {args.date.title()}'
	if args.subject: cri += f'SUBJECT "{args.subject}"'
	if args.sender: cri += f'FROM "{args.sender}"'
	if args.to: cri += f'TO "{args.to}"'
	if args.text: cri += f'TEXT "{args.text}"'
	return cri

def check(user, arg):

	print("Connecting..")
	with imaplib.IMAP4_SSL(IMAP_SERVER) as imap:
		imap.login(user.address, user.app_password)
		box = select_mailbox(imap, arg.box)
		if not box:
			mailbox_error(arg.box)
			return

		imap.select(box)
		CRI = generate_criteria(arg)

		if arg.list and box == "Inbox" and not CRI:
			print("Mailboxes list:")
			for mb in imap.list()[1]: print('\t' + mb.decode().split(' "/" ')[1])
			return
		try:
			_, msgnums = imap.search(None, CRI)
		except Exception:
			criteria_error(CRI)
			return
		if not msgnums[0]:
			print(f"No search results in [{arg.box}].")
			return
		for num in msgnums[0].split():
			_, data = imap.fetch(num, PARTS)
			message = email.message_from_bytes(data[0][1])

			subject = decode_message(message.get('Subject'))
			sender = decode_message(message.get('From'))
			to = message.get('To')
			date = message.get('Date')
			if arg.list:
				print(f" [Subject: {subject}] [From: {sender}] [Date: {date}]")
				continue

			print("\nSubject:\t".expandtabs(11), subject)
			print("From:\t".expandtabs(11), sender)
			print("To:\t".expandtabs(11), to)
			print("Date:\t".expandtabs(11), date)
			body = ""
			attachments = []
			if message.is_multipart():
				for part in message.get_payload():
					ctype = part.get_content_type()
					cdispo = str(part.get('Content-Disposition'))
					content = part.get_payload()
					if ctype in ['text/plain', 'multipart/alternative', 'text/html']:
						if type(content) != str:
							if ctype == 'text/plain': content = content[0]
							else: content = content[1].get_payload()
						body += '\n' + decode_message(content)
					elif 'attachment' in cdispo:
						attachments.append('\t' + part.get_filename())
				if attachments: body += '\nincludes:\n' + '\n'.join(attachments)
			else:
				body += message.get_payload(decode=False)
			print('', body.strip(), LINE, sep='\n')

def delete(user, arg):
	
	print("Connecting..")
	with imaplib.IMAP4_SSL(IMAP_SERVER) as imap:
		imap.login(user.address, user.app_password)
		box = select_mailbox(imap, arg.box)
		if not box:
			mailbox_error(arg.box)
			return
			
		imap.select(box)
		CRI = generate_criteria(arg)
		try:
			_, msgnums = imap.search(None, CRI)
		except Exception:
			criteria_error(CRI)
			return
		if not msgnums[0]:
			print(f"No search results in [{arg.box}].")
			return
		print(f"Deleting selected mails from {box}:")
		count = 0
		for mail in msgnums[0].split():
			# mark the mail as deleted
			imap.store(mail, "+FLAGS", "\\Deleted")

			_, data = imap.fetch(mail, PARTS)
			message = email.message_from_bytes(data[0][1])
			print(f"  email[Subj: {decode_message(message.get('Subject'))}] [From: {decode_message(message.get('From'))}]", "is deleted.")
			count += 1

		print(count, f"selected email{'s have' if count > 1 else ' has'} been deleted.\n")

