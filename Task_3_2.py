# Task 2

def user_info(name, surname, birth, location, email, mob):
    return f"Привет, {name} {surname}! С Днем Рождения! {birth} родился такой отличный ДРУГ, как ТЫ!!!" \
           f" Я пытался дозвониться по номеру в telegram: {mob}; а также пробовал писать на:" \
           f" {email}. Но, к сожалению, ты так и не вернулся домой, в г. {location}. Позвони мне!!!"


print(user_info(name='Nikolay', surname='Sviridov', birth='??.??.1991', location='Москва', email='n.luchanos@gmail.com',
                mob='@Luchanos'))
