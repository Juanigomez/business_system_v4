# BUSINESS SYSTEM v4 - pynet | juanigomez

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image as img

navBar = option_menu(

    menu_title = None,
    options = ["Homepage", "Database", "Purchase", "Sales"],
    icons = ["house", "folder2", "cart3","database-check"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal"

)

def get_Data(filename):
    data = pd.read_csv(filename)
    return data

def get_Index(value, all_Values):

    index = 0
    count = int(len(all_Values) - 1)

    if value != all_Values[index]:
        for n in all_Values:
            while value != all_Values[index]:
                if index == count:
                    break
                else:
                    index += 1

    return index

def Homepage():

    st.title("Business System: ")
    logo = img.open('pynet_logo_complete.png')
    st.image(logo)

def Database():

    def Customers():

        header = st.container()
        inputs = st.container()
        button = st.container()
        table = st.container()

        with header:

            st.title("Customer Information")
            st.text("Input and access customer information.")

        with inputs:

            col1, col2 = st.columns(2)

            with col1:

                Name = str(st.text_input("Enter customer name: "))
                rut = st.text_input("Customer RUT: ")
                total_Spent = int(0)
                st.text("Plata gastada: ")
                money_Spent = st.error(f"$ {total_Spent}")

            with col2:

                Address = st.text_input("Enter customer address: ")
                Phone_Number = st.text_input("Enter customer phone number: ")
                mail = st.text_input("Enter customer e-mail: ")

        with button:

            customer_input_btn = st.button("Submit")
            if customer_input_btn:
                
                global customers_Dataset
                customers_Dataset = get_Data('customers.csv')

                all_Customers = list(customers_Dataset.iloc[:,0])
                index = get_Index(Name, all_Customers)

                if Name == all_Customers[index]:

                    current_Customer = Name
                    st.error(f"Known customer: {current_Customer}")

                    def update_Customer_Data():

                        df = get_Data('customers.csv') 

                        df.loc[index, 'NOMBRE'] = Name
                        df.loc[index, 'RUT'] = rut
                        df.loc[index, 'DIRECCION'] = Address
                        df.loc[index, 'CELULAR'] = Phone_Number
                        df.loc[index, 'MAIL'] = mail
                        df.loc[index, 'PLATA GASTADA'] = money_Spent
                        
                        df.to_csv('customers.csv',index=False)

                    update_Customer_Data()

                else:
                    new_data = [[Name, rut, Address, Phone_Number, mail, money_Spent]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('customers.csv', mode='a', index=False, header=False)

                    current_Customer = Name
                    st.error(f"New customer: {current_Customer}")

        with table:

            st.subheader("Customer dataset")
            st.text("Table containing customer information: ")

            customers_Table = get_Data('customers.csv')
            st.write(customers_Table)

    def Products():

        header = st.container()
        inputs = st.container()
        button = st.container()
        table = st.container()

        with header:

            st.title("Product Information")
            st.text("Input and access product information.")

        with inputs:

            col1, col2 = st.columns(2)

            with col1:

                Name = st.text_input("Enter product name: ")
                Stock = int(st.slider("Enter product stock: "))
                Supplier = st.text_input("Enter product supplier: ")

            with col2:

                Price = int(st.number_input("Enter product price: ", step=100))
                Cost = int(st.number_input("Enter product cost: ", step=100))
                Margin = int(Price - Cost)
                st.text("Product Margin: ")
                st.error(Margin)

        with button:

            product_input_btn = st.button("Submit")
            if product_input_btn:

                global products_Dataset
                products_Dataset = get_Data('products.csv')

                all_Products = list(products_Dataset.iloc[:,0])
                index = get_Index(Name, all_Products)

                if Name == all_Products[index]:
                    current_Product = Name
                    st.error(f"Known product: {current_Product}")

                    def update_Product_Data():

                        df = get_Data('products.csv') 

                        df.loc[index, '    NOMBRE    '] = Name
                        df.loc[index, 'STOCK'] = Stock
                        df.loc[index, 'PRECIO'] = Price
                        df.loc[index, 'COSTE'] = Cost
                        df.loc[index, 'MARGEN'] = Margin
                        df.loc[index, '    PROVEEDOR    '] = Supplier
                        
                        df.to_csv('products.csv',index=False)

                    update_Product_Data()

                else:
                    new_data = [[Name, Stock, Price, Cost, Margin, Supplier]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('products.csv', mode='a', index=False, header=False)

                    current_Product = Name
                    st.error(f"New Product: {current_Product}")

        with table:

            st.subheader("Product dataset")
            st.text("Table containing product information: ")

            products_Table = get_Data('products.csv')
            st.table(products_Table)

    def Employees():
            
            header = st.container()
            inputs = st.container()
            button = st.container()
            table = st.container()

            with header:

                st.title("Employee Information")
                st.text("Input and access employee information.")

            with inputs:

                col1, col2, col3 = st.columns(3)

                with col1:

                    Name = st.text_input("Enter employee name: ")
                    Address = st.text_input("Enter employee address: ")
                    Phone_Number = st.text_input("Enter employee phone number: ")

                with col2:

                    Position = st.selectbox("Enter employee charge: ", ['Salesman', 'Accountant', 'Cashier'])
                    piece_Rate = int(st.slider("Piece rate percenatge: ", min_value=0, max_value=100, step=1))
                    time_Rate = int(st.number_input("Enter time rate amount: ", step=1))

                with col3:

                    hours_Week = int(st.number_input("Enter hours worked a week: ", step=1))

                    st.text("Wage and Salary: ")

                    wage = int(time_Rate * hours_Week)
                    st.error(f"Wage: $ {wage}")

                    salary = int(wage * 4)
                    st.error(f"Salary: $ {salary}")

            with button:

                product_input_btn = st.button("Submit")
                if product_input_btn:

                    global employees_Dataset
                    employees_Dataset = get_Data('employees.csv')

                    all_Employees = list(employees_Dataset.iloc[:,0])
                    index = get_Index(Name, all_Employees)

                    if Name == all_Employees[index]:
                        current_Employee = Name
                        st.error(f"Known employee: {current_Employee}")

                        def update_Employee_Data():

                            df = get_Data('employees.csv') 

                            df.loc[index, 'NOMBRE'] = Name
                            df.loc[index, 'DIRECCION'] = Address
                            df.loc[index, 'CELULAR'] = Phone_Number
                            df.loc[index, 'POSICION'] = Position
                            df.loc[index, '$/HORA'] = time_Rate
                            df.loc[index, 'COMISION'] = piece_Rate
                            df.loc[index, 'HORAS SEMANALES'] = hours_Week
                            df.loc[index, 'SALARIO'] = salary
                            
                            df.to_csv('employees.csv',index=False)

                        update_Employee_Data()

                    else:
                        new_data = [[Name, Address, Phone_Number, Position, time_Rate, piece_Rate, hours_Week, salary]]
                        df = pd.DataFrame(new_data)
                        df.to_csv('employees.csv', mode='a', index=False, header=False)

                        current_Employee = Name
                        st.error(f"New Employee: {current_Employee}")

            with table:

                st.subheader("Employees dataset")
                st.text("Table containing employee information: ")

                employees_Table = get_Data('employees.csv')
                st.table(employees_Table)

    def Discounts():

        header = st.container()
        inputs = st.container()
        table = st.container()

        with header:

            st.header("Discount Information")
            st.text("Input and access discount information.")

        with inputs:

            st.subheader("Data Input")

            Name = st.text_input("Enter discount name: ")
            Percentage = st.slider("Discount", 5, 100, step=5)
            Reason = st.text_input("Enter discount reason: ")

            discount_input_btn = st.button("Submit")
            if discount_input_btn:

                global discounts_Dataset
                discounts_Dataset = pd.read_csv('discounts.csv')

                all_Discounts = list(discounts_Dataset.iloc[:,0])
                index = get_Index(Name, all_Discounts)

                if Name == all_Discounts[index]:

                    current_Discount = Name
                    st.error(f"Known discount: {current_Discount}")

                    def update_Discount_Data():

                        df = get_Data('discounts.csv') 

                        df.loc[index, 'NOMBRE   '] = Name
                        df.loc[index, 'DESCUENTO'] = Percentage
                        df.loc[index, 'MOTIVO          '] = Reason
                        
                        df.to_csv('discounts.csv',index=False)

                    update_Discount_Data()

                else:
                    new_data = [[Name, Percentage, Reason]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('discounts.csv', mode='a', index=False, header=False)

                    current_Customer = Name
                    st.error(f"New discount: {current_Customer}")

        with table:
             
            st.header("Discounts Dataset")
            st.text("Table containing discount infomation:")
            st.table('discounts.csv')

    all_Pages = {
    "Customers": Customers,
    "Products": Products,
    "Employees": Employees,
    "Discounts": Discounts
}
    st.sidebar.title("Python Website")
    st.sidebar.header("Databse structure")

    selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
    all_Pages[selected_page]()

def Purchase():

    header = st.container()
    employee_Input = st.container()
    inputs = st.container()

    with header:

        st.title("Purchase Input")

    with employee_Input:

        st.text_input("Enter employee name: ")

    with inputs:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.subheader("Customer Info.")
            current_Customer = st.text_input("Customer name: ")

            all_Customers = list(customers_Dataset.iloc[:,0])
            customer_Index = get_Index(current_Customer, all_Customers)

            if current_Customer == all_Customers[customer_Index]:

                def get_Address():

                    all_Addresses = list(customers_Dataset.iloc[:,2])
                    current_Address = all_Addresses[customer_Index]
                    st.error(current_Address)

                get_Address()

                def get_Phone_Number():

                    all_Phone_Numbers = list(customers_Dataset.iloc[:,3])
                    current_Phone_Number = all_Phone_Numbers[customer_Index]
                    st.error(f"Phone Number: {current_Phone_Number}")

                get_Phone_Number()

            else: st.text("")

        with col2:

            st.subheader("Product Info.")
            current_Product = st.text_input("Product name: ")
            current_Amount = st.slider("Amount", 1, 50)

            all_Products = list(products_Dataset.iloc[:,0])
            product_Index = get_Index(current_Product, all_Products)

            if current_Product == all_Products[product_Index]:

                def get_Price():

                    all_Prices = list(products_Dataset.iloc[:,2])
                    global current_Price
                    current_Price = int(all_Prices[product_Index])
                    st.text(f"Price: {current_Price}")

                get_Price()

                def get_Stock():

                    all_Stocks = list(products_Dataset.iloc[:,1])
                    global current_Stock
                    current_Stock = all_Stocks[product_Index]

                get_Stock()

                def calculate_Price():

                    global total_Price
                    total_Price = int(current_Price * current_Amount)
                    st.text(f"Total: {total_Price}")

                calculate_Price()

            else: st.text("")

        with col3:

            st.subheader("Payment Info.")

            method = st.text_input("Payment method: ")
            all_Discounts = list(discounts_Dataset.iloc[:,0])
            current_Discount = str(st.selectbox("Select discount: ", all_Discounts))

            discount_Index = get_Data(current_Discount, all_Discounts)

            if current_Product == None:
                st.text("")
            else:
                if discount_Index == 0:
                    st.error("No discount")
                    st.error(f" --> $ {total_Price}")
                else:

                    if current_Discount == all_Discounts[discount_Index]:
                        
                        def get_Percentage():

                            all_Percentages = list(discounts_Dataset.iloc[:,1])
                            global current_Percentage
                            current_Percentage = all_Percentages[discount_Index]

                        get_Percentage()

                        def show_Discount_Price():

                            sub = int((current_Percentage * total_Price)/ 100)

                            global discount_Price
                            discount_Price = int(total_Price - sub)

                            st.error(f"Discount: {current_Percentage}: {sub}")
                            st.error(f"Discount price: {discount_Price}")

                        show_Discount_Price()  

                    else: st.text("")

def Sales():

    header = st.container()
    table = st.container()

    with header:

        st.title("Sales history")
        st.text("On this page you are able to access the purchase dataset: ")

    with table:

        sales_Dataset = get_Data('sales.csv')
        st.table(sales_Dataset)

if navBar == "Homepage":
    Homepage()

elif navBar == "Database":
    Database()
    
elif navBar == "Purchase":
    Purchase()

elif navBar == "Sales":
    Sales()
