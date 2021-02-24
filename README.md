# Shopping Cart Exercise

This is the README.md file. It explains what this program is and how to run the program. 

## What does *Shoppers'* program do?

The program includes a list of items that a customer at *Shoppers* might encounter walking through the aisles of the supermarket. Therefore, this program acts as a virtual cashier. It asks first for the identifier of the prodcut so that it would know which product it is and whether it is priced per pound or per item. After knowing that, it asks the customer how many pounds or items of the product they want, which makes it a quicker way than scanning each and every single product (if they're any duplicates). So, in the end, the program generates a receipt for the customer and asks them whether they would want a copy of the receipt sent via email and made as a txt file. 

## Where to start? 

### Repository Setup

Upon the download of the repository, preferably onto customer's desktop, the customer must open their command-line (in Mac case: Terminal) and make sure that the working directory is currently their desktop by typing the following line: 
 
 ```sh
cd ~/Desktop/shopping-cart
```

### Environment Setup

This program requires the customer to create a virtual environment using Anaconda. Therefore, the customer might create the following environment in their command-line by typing the following lines of code:

```sh
conda create -n my-shopping-env python=3.8
conda activate my-shopping-env
```

### Installing the packages

This program requires third party packages in order to run some code such as sending the receipt via email for example. The third party packages are already stored in a file called *requirements.txt* and therefore the customer must run the following line of code in their command-line:

```sh
pip install -r requirements.txt
```

After completing these three steps, the customer is now ready to shop and see how much they are supposed to pay via a receipt generated by the program. 

## Further Explorations

The program allows the customer to change the tax rate based on where they are living. In the *.env* file, there is a variable called *TAX_RATE*. Hence, to change the rate, the customer must access the file and write the percentage in terms of a decimal as already shown by the default rate of 0.0875 and that will automatically change the tax rate for the program to process (after saving the file).

Moreover, the program allows the customer to generate a txt file version of their receipt and also have access to it via email. This is also created using the *.env* file. In conclusion, this program allows the customer to more than just generate a simple receipt but has added value which allows for a smoother checking out (at the cashier process). 