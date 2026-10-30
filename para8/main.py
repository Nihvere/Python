with open('shopping.txt', 'r', encoding='utf-8') as f:
    content = f.read().strip()

with open('transfer.txt', 'w', encoding='utf-8') as transfer:
    updated_content = content.replace('старое слово', 'новое слово')
    transfer.write(updated_content)

with open('transfer.txt', 'r', encoding='utf-8') as transfer:
    print(transfer.read())