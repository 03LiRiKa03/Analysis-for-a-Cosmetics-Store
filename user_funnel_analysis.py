import pandas as pd

df = pd.read_csv("file")
df = df.sort_values(by=['user_session', 'event_time'])

event_counts = df['event_type'].value_counts()
print(event_counts)

total_users = df['user_id'].nunique() 
view_users = df[df['event_type']=='view']['user_id'].nunique()
cart_users = df[df['event_type']=='cart']['user_id'].nunique()
purchase_users = df[df['event_type']=='purchase']['user_id'].nunique()

print("Total users:", total_users)
print("Viewed:", view_users, "-", round(view_users/total_users*100,2), "%")
print("Added to cart:", cart_users, "-", round(cart_users/total_users*100,2), "%")
print("Purchased:", purchase_users, "-", round(purchase_users/total_users*100,2), "%")
