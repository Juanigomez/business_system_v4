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
            discounts_Dataset = get_Data('discounts.csv')
            st.table(discounts_Dataset)

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
    id_inputs = st.container()
    inputs = st.container()
    button = st.container()
    output = st.container()

    with header:

        st.title("Purchase Input")

    with id_inputs:

        current_Employee = st.text_input("Employee Name: ")
        current_Customer = st.text_input("Customer Name: ")

        def get_Customer_Data():

                customers_Dataset = pd.read_csv('customers.csv')
                all_Customers = list(customers_Dataset.iloc[:,0])
                customer_Index = get_Index(current_Customer, all_Customers)

                if current_Customer == all_Customers[customer_Index]:
  
                    # GET RUT:
                    all_RUTs = list(customers_Dataset.iloc[:,1])
                    global current_RUT
                    current_RUT = all_RUTs[customer_Index]

                    # GET ADDRESS:
                    all_Addresses = list(customers_Dataset.iloc[:,2])
                    current_Address = all_Addresses[customer_Index]

                    # GET PHONE NUMBER:
                    all_Phone_Numbers = list(customers_Dataset.iloc[:,3])
                    current_Phone_Number = all_Phone_Numbers[customer_Index]

                else: st.text("")

    with inputs:

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Product Info. ")
            current_Product = st.text_input("Product Name: ")
            current_Amount = st.slider("Amount", 1, 100)

            def get_Product_Data():

                products_Dataset = pd.read_csv('products.csv')
                all_Products = list(products_Dataset.iloc[:,0])
                product_Index = get_Index(current_Product, all_Products)

                if current_Product == all_Products[product_Index]:

                        # GET PRICE:
                        all_Prices = list(products_Dataset.iloc[:,2])
                        global current_Price
                        current_Price = int(all_Prices[product_Index])

                        # GET STOCK:
                        all_Stocks = list(products_Dataset.iloc[:,1])
                        global current_Stock
                        current_Stock = all_Stocks[product_Index]

                        # CALCULATE TOTAL PRICE:
                        global total_Price
                        total_Price = int(current_Price * current_Amount)

                else: st.text("")

        with col2:

            st.subheader("Payment Info. ")
            current_Method = st.selectbox("Select Method: ", ['efectivo, debito, credito'])
            current_Cuotas = st.select_slider("Cuotas", [0, 2, 3, 4])
            
            discounts_Dataset = get_Data('discounts.csv')
            all_Discounts = discounts_Dataset.iloc[:,0]

            current_Discount = st.selectbox("Select Discount: ", all_Discounts)

            def get_Discount_Data():

                discount_Index = get_Index(current_Discount, all_Discounts)

                if current_Discount == all_Discounts[discount_Index]:
                        
                    # GET PERCENTAGE:
                    all_Percentages = list(discounts_Dataset.iloc[:,1])
                    global current_Percentage
                    current_Percentage = all_Percentages[discount_Index]

                    # CALCULATE DISCOUNT PRICE:
                    global sub
                    sub = int((current_Percentage * total_Price)/ 100)
                    global discount_Price
                    discount_Price = int(total_Price - sub)

                else: st.text("")

    with button:

        run_Btn = st.button("Submit")
        if run_Btn:

            get_Customer_Data()  

            get_Product_Data()

            get_Discount_Data()

    with output:

        id_Outputs = st.container()
        purchase_Return = st.container()
        button = st.container()

        with id_Outputs:

            sales, purchases = "-"
            st.error(f"Employee name: {current_Employee}, number of sales: {sales}")
            st.error(f"Customer: {current_Customer}, RUT: {current_RUT}, purchases: {purchases}")

        with purchase_Return:

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Product Info. ")
                st.error(f"Product: {current_Product}")
                st.error(f"Amount: {current_Amount}")
                st.error(f"Precio: {current_Price}")
                st.text("")
                st.success(f"TOTAL: {total_Price}")

            with col2:

                st.subheader("Payment Info.")
                st.error(f"Method: {current_Method}")
                st.error(f"Cuotas: {current_Cuotas}")
                st.error(f"Discount: {current_Percentage}, ({sub})")
                st.text("")
                st.success(f"TOTAL(%): {discount_Price}")

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
