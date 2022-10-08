from tkinter import messagebox


# This implementation use only one asset. For more we purpose
# another method of tkinter.

def message_alert(asset, price):
    return messagebox.showinfo(f"{asset}", f"Target the price{price}")


if __name__ == '__main__':
    message_alert(asset='MSFT', price=56.89)
