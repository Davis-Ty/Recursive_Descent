from csci3333tok import Tokenizer 
import inspect#checking what function called current function
def expr(nt):#(Function)
	lexeme=nt.text
	token=nt.name	
	if(token=='EOS' ):
		print("Exiting expr")
	elif(lexeme=='*' or lexeme=='/'):	
		print("Exiting expr")
		factor(nt)
	elif(lexeme=='-' or lexeme=='+'):
			if(inspect.stack()[1][3]!="term"):
				print("Entering EXPR")
			elif(lexeme=='-'):
				print('Matched '+ token+ ' selected - ...skipping')
				t.lex()
				nt = t.next_token()
				print('next token is '+nt.name)
				expr(nt)#term(nt)
			else:
				print('Matched '+ token+ ' selected + ...skipping')
				t.lex()
				nt = t.next_token()
				print('next token is '+nt.name)
				expr(nt)#term(nt)								
	else:	
			if(inspect.stack()[1][3]!="expr" and inspect.stack()[1][3]!="term"):
				print("Entering EXPR") 
				term(nt)#print("Exiting expr")
			else:
				try:
					int(lexeme)
					term(nt)
				except:
					print("Exiting expr")
					factor(nt)


def term(nt):#(Function)term
	lexeme=nt.text
	token=nt.name
	if(token=='EOS' or lexeme=='+' or lexeme=='-'):
		print("Exiting term")
		expr(nt) 
	elif(lexeme=='*' or lexeme=='/'):
		if (lexeme=='*'):
			print('Matched '+ token+ ' selected * ...skipping')
			t.lex()
			nt = t.next_token()
			print('next token is '+nt.name)
			#print("Exiting term")
			expr(nt) #factor(nt)
		else:
			print('Matched '+token+ ' selected / ...skipping')
			t.lex()
			nt = t.next_token()
			print('next token is '+nt.name)
			#print("Exiting term")
			expr(nt)#factor(nt)
	else:
		if(inspect.stack()[1][3]=="factor"):
			print("Exiting term")
			expr(nt)
		else:
			print("Entering TERM")
			factor(nt)

def factor(nt):#(Function)term
	lexeme=nt.text
	token=nt.name
	if not (lexeme=='/' or lexeme=='*' or token=='EOS' or lexeme=='+' or lexeme=='-' ):#checking what the lexeme and calling the right function
		if(inspect.stack()[1][3]=="factor"):
			if(lexeme!=')'):
				expr(nt)
			else:
				print("Exiting factor")
				term(nt)
		else:
			if(inspect.stack()[1][3]!="expr"):
				print("Entering factor")
			print('Matched '+ token+ ' selected '+lexeme+'...skipping')
			t.lex()
			nt = t.next_token()
			print('next token is '+nt.name)
			#print("Exiting factor")
			factor(nt)	
	else:
		print("Exiting factor")
		term(nt)

if __name__=='__main__':#main line
	t=Tokenizer()
	t.tokenize('(5 + 3) * 2')
	nt = t.next_token()
	print('next token is '+nt.name)
	expr(nt)
