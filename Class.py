class PythonClass :
    def __init__(this):
        this.dataEntered: dict[str, str] = {
            'dev': 'Araby'
        }

    def setUser(this: 'PythonClass', user: dict[str, str | int]) :
        this.dataEntered['username'] = user['username'];
        this.dataEntered['age'] = user['age'];    
        this.dataEntered['mail'] = user['mail'];


    def __str__(this) -> str:
        return f"{this.dataEntered['Class']}";

py = PythonClass();
py.setUser({
    'username': 'brian',
    'age': 19,
    'mail': 'mehmet@araby.tr'
});

print(f"Username → {py.dataEntered['username']}");
print(f"Age → {py.dataEntered['age']}");
print(f"Email Address → {py.dataEntered['mail']}");