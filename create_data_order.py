import pandas as pd
import numpy as np
from faker import Faker

# Set seed

Faker.seed(42)

# create some fake data
fake = Faker()

# ### We will try to create a table with the following schema::

# CREATE TABLE om_order_header (

#   order_id NUMBER NOT NULL,

#   customer_id NUMBER NOT NULL,

#   order_date DATE NOT NULL,

#   order_status VARCHAR2(255) NOT NULL,

#   total_amount NUMBER NOT NULL,

#   PRIMARY KEY (order_id)

# );

# function to create a dataframe with fake values for our workers
def make_workers():
    
    order_status_list = ['canceled', 'placed', 'pending', 'delivered']

    fake_workers = [{'order_id': np.random.randint(1,10000000),
                     'customer_id': np.random.randint(1,10000000),
        'order_date': fake.date(), 
        'order_status': np.random.choice(order_status_list),
        'total_amount': np.random.randint(1,1000)
     }]
        
    return fake_workers

def append_to_df(n):
    
    worker_df = pd.DataFrame(make_workers())
    
    i=1
    while i < n:
        worker_df = worker_df.append(pd.DataFrame(make_workers()))
        i += 1 
    
    worker_df.reset_index(inplace=True, drop=True)
    
    return worker_df


if __name__ == "__main__":
    
    # Generating output
    
    print("Generating output")
    print()
    
    output_df = append_to_df(100)
    
    # Writing output to disk
    
    print("Writing output to disk")
    print()
    
    output_df.to_csv('data_sample.csv', index=False)
    
    
    
    