from PIL import Image, ImageFilter

print("hello world: ", "jinkejk")
print(3/9)
print(3//9)
print(chr(66))
print(ord('D'))
print(chr(25991))
print('sadada%s,%d' % ('jinke',322))

people = ['das','sad','daada']
print(people.__len__())
print(people.__getitem__(-1))
print(people.pop(1))
people.append(21)
print(people)

t = (12,211)
print(t[0])

print(int('21'))

for i in range(20):
    print(i)

print(i)

while i>10:
    print(i)
    i -= 1
    if i == 15:
        print(i, '---end')
        break

#json? dict
d = {'jink' : 21, 'dad' : 33}
print(d['jink'])
print('sada' in d)
print(d.get('jinks', '........'))

im = Image.open('../data/timg.jpeg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('../data/blue.jpg', 'jpeg')
im2.show()




