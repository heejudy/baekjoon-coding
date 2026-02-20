while True:
  stack = []
  string = input()
  if string == '.':
    break
  else:
    for s in string: 
      if s == '(' or s == '[':
        stack.append(s)
      else:
        if s == ')':
          if len(stack) == 0:
            stack.append(s)
            break

          if stack[-1] == '(':
            stack.pop(-1)
          else:
            stack.append(s)

        elif s == ']':
          if len(stack) == 0:
            stack.append(s)
            break

          if stack[-1] == '[':
            stack.pop(-1)
          else:
            stack.append(s)

  if stack == []:
    print("yes")
  else:  
    print("no")
