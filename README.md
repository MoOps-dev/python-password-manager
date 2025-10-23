# Python Password Manager
Password manager is a tool to save user credentials for various websites and store them in an organized way easy to view
and manage by the user. It also helps the user generate a strong password so your credentials are always strong and secure.

## Language practices within this project:
- Tkinter library   
- GUI with Tkinter
- OOP
- Keyword arguments with '**kwargs'
- Lists, dictionaries, loops
- Random password generation
- List comprehension:

    ```` python
        password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
        password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
        password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    ````
- Working with CSV files using Pandas library:
  - Creating a CSV file:
  
    ```` python
        if not os.path.isfile("book.csv"):
            file = pd.DataFrame(columns=["id", "website", "username", "password"])
            file.to_csv('book.csv', index=False)
    ````
  - Reading the data from the CSV file:
  
    ```` python
        df = pd.read_csv('book.csv', index_col=0)

        for index, row in df.iterrows():
            # set each record from the data file to a parent value and credentials under it in the tree
            parent_id = self.bw_list.insert('', 'end', text=f'{index}. {row['website']}', values=([f"-{index}"]))
            self.bw_list.insert(parent_id, 'end', text=f"User: {row['username']}", values=(["+"]))
            self.bw_list.insert(parent_id, 'end', text=f"Password: {row['password']}", values=(["++"]))
    ````
  - Saving new data to the CSV file:
  
    ```` python
        data_strct = {
                "website" : [self.website.get()],
                "user" : [self.user.get()],
                "password" : [self.password.get()]
            }

        # read the last index of the last row or set the index to zero if there are not records
        existing_df = pd.read_csv('book.csv', index_col=0)
        if existing_df.index.empty:
            last_index = 0
        else:
            last_index = existing_df.index.max()

        # save the data from the app fields to the csv file
        new_data = pd.DataFrame(data_strct)
        new_data.index = range(last_index + 1, last_index + 1 + len(new_data))
        new_data.to_csv('book.csv', mode='a', header=False)
    ````
    
## App Features:
- Save user credentials containing Website, Username/Email and Password
- Generate a random password upon request and copy it to clipboard instantly
- Save all the credential to the Book window
- The ability to delete saved data from the book window
- Copy the username or password from the book window to clipboard once clicked

## App Preview:

![Python Password Manager](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjk1cXVsMWw4bnRkaHphNGRwMzhpcmk5bmVwbWRuN3N0cjh6dXVzNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hhQzdvbyd3sT5fEirI/giphy.gif)

![Python Password Manager](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGRyazNxb2p6YzBjYWJtZmRkMWU3YWVvYjNsaTd5aWZ6aHNoanhuaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jq2EtwQJn9Qa0PaKxI/giphy.gif)