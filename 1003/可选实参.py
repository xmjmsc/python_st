def get_formatted_name(first_name, last_name, middle_name=''):
    #设定默认值的实参须在末尾 
#返回整洁的姓名 
    if middle_name: 
        full_name = first_name + ' ' + middle_name + ' ' + last_name 
    else: 
        full_name = first_name + ' ' + last_name 
    return full_name.title() 

musician = get_formatted_name('jimi', 'hendrix') 
print(musician) 
musician = get_formatted_name('john', 'hooker', 'lee') 
print(musician) 


def build_person(first_name, last_name, age=''): 
    #"""返回一个字典，其中包含有关一个人的信息""" 
    person = {'first': first_name, 'last': last_name} 
    if age: 
        person['age'] = age 
        #如果有age，则在列表person中添加一项'age'
    return person 
musician = build_person('jimi', 'hendrix', age=27) 
print(musician)