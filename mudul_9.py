def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'Contact with this name does not exist'
        except ValueError:
            return 'Please enter your name and phone number'
        except IndexError:
            return 'Enter your username'
    return inner

@error_handler
def add(*args, **kwargs):
    name, phone = args
    user[name] = phone

def change(*args, **kwargs):
    name, phone = args
    user[name] = phone

def phone(*args, **kwargs):
    name = args[0]
    return user.get(name, 'Contact not found')

def show_all():
    return user

def main():
    while True:
        command = input('Enter the command: ').lower()
        
        if command == 'hello':
            print('How can I help you?')
        elif command.startswith('add'):
            _, name, phone = command.split(' ')
            add(name, phone)
        elif command.startswith('change'):
            _, name, phone = command.split(' ')
            change(name, phone)
        elif command.startswith('phone'):
            _, name = command.split(' ')
            print(phone(name))
        elif command == 'show all':
            print(show_all())
        elif command in ['good bye', 'close', 'exit']:
            print('Goodbye!')
            break
        else:
            print('Unknown request. Try again.')

user = {}

if __name__ == "__main__":
    main()
