

def echo(text: str, repetitions: int = 3) -> str:
	res = ""
	for i in reversed(range(1,repetitions+1)):
		res += text[len(text)-i:] + "\n"
	res += "."
	
	return res

if __name__ == "__main__":
	text = input("Yell something at a mountain: ")
	print(echo(text))