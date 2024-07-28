import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data/tcas.csv')

# Filter rows where the 'major', 'minor', 'course', or 'course_name' columns contain the keyword 'วิศวกรรม'
major_df = df[df['major'].str.contains('วิศวกรรม', na=False)]
minor_df = df[df['minor'].str.contains('วิศวกรรม', na=False)]
course_df = df[df['course'].str.contains('วิศวกรรม', na=False)]
course_name_df = df[df['course_name'].str.contains('วิศวกรรม', na=False)]

# Combine the filtered DataFrames and remove duplicates
combine_df = pd.concat([major_df, minor_df, course_df, course_name_df])
combine_df = combine_df.drop_duplicates()

# Columns to delete from the combined DataFrame
delete_columns = ['web-scraper-order', 'web-scraper-start-url', 'uni-href', 'major-href', 'minor-href', 'course-href', 'course_name']
c_df = combine_df.drop(columns=delete_columns)

# Clean up specific columns by removing numerical prefixes and extracting numerical values
c_df['major'] = c_df['major'].str.replace(r'\d+\.\s*', '', regex=True)
c_df['minor'] = c_df['minor'].str.replace(r'\d+\.\s*', '', regex=True)
c_df['course'] = c_df['course'].str.replace(r'\d+\.\s*', '', regex=True)
c_df['fee'] = c_df['fee'].str.extract(r'(\d[\d,]*)').replace(',', '', regex=True)
c_df['success_rate'] = c_df['success_rate'].str.extract(r'(\b\d{1,3}\b)')
c_df['round1'] = c_df['round1'].str.extract(r'(\d+)')
c_df['round2'] = c_df['round2'].str.extract(r'(\d+)')
c_df['round3'] = c_df['round3'].str.extract(r'(\d+)')
c_df['round4'] = c_df['round4'].str.extract(r'(\d+)')
c_df = c_df.fillna(0)

# Convert columns to appropriate data types
c_df['fee'] = c_df['fee'].astype(int)
c_df['success_rate'] = c_df['success_rate'].astype(int)
c_df['round1'] = c_df['round1'].astype(int)
c_df['round2'] = c_df['round2'].astype(int)
c_df['round3'] = c_df['round3'].astype(int)
c_df['round4'] = c_df['round4'].astype(int)

# Adjust fees to a minimum value if they are less than 80,000
c_df.loc[c_df['fee'] < 80000, 'fee'] = c_df['fee'] * 8

# Create a DataFrame with university names and their corresponding latitude and longitude values
data = {
    'uni': ['สถาบันการจัดการปัญญาภิวัฒน์', 'มหาวิทยาลัยหอการค้าไทย', 'มหาวิทยาลัยสยาม', 'มหาวิทยาลัยศรีปทุม', 'มหาวิทยาลัยรังสิต', 'มหาวิทยาลัยปทุมธานี', 'มหาวิทยาลัยธุรกิจบัณฑิตย์', 'มหาวิทยาลัยเทคโนโลยีมหานคร', 'มหาวิทยาลัยเกษมบัณฑิต', 'มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน', 'มหาวิทยาลัยเทคโนโลยีราชมงคลศรีวิชัย', 'มหาวิทยาลัยเทคโนโลยีราชมงคลรัตนโกสินทร์', 'มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี', 'มหาวิทยาลัยเทคโนโลยีราชมงคลตะวันออก', 'มหาวิทยาลัยเทคโนโลยีราชมงคลกรุงเทพ', 'มหาวิทยาลัยราชภัฏสวนสุนันทา', 'มหาวิทยาลัยราชภัฏเพชรบุรี', 'มหาวิทยาลัยราชภัฏบ้านสมเด็จเจ้าพระยา', 'มหาวิทยาลัยราชภัฏชัยภูมิ', 'สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง', 'มหาวิทยาลัยอุบลราชธานี', 'มหาวิทยาลัยสงขลานครินทร์', 'มหาวิทยาลัยศิลปากร', 'มหาวิทยาลัยศรีนครินทรวิโรฒ', 'มหาวิทยาลัยวลัยลักษณ์', 'มหาวิทยาลัยรามคำแหง', 'มหาวิทยาลัยแม่โจ้', 'มหาวิทยาลัยมหาสารคาม', 'มหาวิทยาลัยมหิดล', 'มหาวิทยาลัยพะเยา', 'มหาวิทยาลัยบูรพา', 'มหาวิทยาลัยนเรศวร', 'มหาวิทยาลัยนราธิวาสราชนครินทร์', 'มหาวิทยาลัยนครพนม', 'มหาวิทยาลัยธรรมศาสตร์', 'มหาวิทยาลัยทักษิณ', 'มหาวิทยาลัยเทคโนโลยีสุรนารี', 'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ', 'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี', 'มหาวิทยาลัยเชียงใหม่', 'มหาวิทยาลัยขอนแก่น', 'มหาวิทยาลัยกาฬสินธุ์', 'มหาวิทยาลัยเกษตรศาสตร์', 'จุฬาลงกรณ์มหาวิทยาลัย', 'มหาวิทยาลัยหัวเฉียวเฉลิมพระเกียรติ', 'มหาวิทยาลัยราชภัฏอุบลราชธานี', 'มหาวิทยาลัยราชภัฏสงขลา', 'มหาวิทยาลัยราชภัฏพระนคร', 'มหาวิทยาลัยราชภัฏพิบูลสงคราม', 'มหาวิทยาลัยราชภัฏนครราชสีมา', 'สถาบันเทคโนโลยีจิตรลดา', 'มหาวิทยาลัยแม่ฟ้าหลวง', 'มหาวิทยาลัยนวมินทราธิราช', 'มหาวิทยาลัยราชภัฏจันทรเกษม'],
    'lat': [13.8879, 13.7671, 13.7202, 13.8751, 13.9642, 13.9787, 13.8222, 13.7261, 13.7380, 15.2186, 7.0085, 13.7380, 14.0272, 13.3445, 13.7260, 13.7769, 13.1098, 13.7252, 15.8022, 13.7293, 15.1288, 7.0085, 13.7796, 13.7537, 8.6537, 13.7487, 18.9350, 16.2498, 13.7925, 19.0294, 13.2822, 16.7487, 6.5427, 17.4065, 14.0737, 7.1070, 14.8838, 13.8234, 13.6520, 18.7961, 16.4735, 16.4322, 13.8468, 13.7384, 13.6551, 15.1187, 7.1723, 13.8323, 16.8218, 14.9780, 13.7670, 20.0258, 13.7514, 13.8204],
    'lon': [100.5114, 100.5516, 100.4769, 100.5828, 100.5858, 100.5319, 100.5288, 100.7920, 100.6114, 104.8574, 100.4750, 100.3278, 100.7752, 100.9847, 100.5167, 100.5042, 99.9427, 100.4928, 102.0272, 100.7797, 104.3221, 100.4741, 100.4906, 100.5625, 99.8960, 100.5923, 98.9480, 103.2480, 100.3233, 99.8955, 100.9267, 100.1955, 101.4181, 104.7813, 100.6069, 100.6068, 102.0194, 100.5135, 100.4941, 98.9523, 102.8207, 103.5065, 100.5697, 100.5329, 100.6868, 104.8840, 100.6123, 100.5687, 100.2624, 102.1232, 100.5101, 99.8953, 100.4941, 100.5731]
}

# Create a DataFrame from the university latitude and longitude data
df_lat_lon = pd.DataFrame(data)

# Merge the cleaned DataFrame with the latitude and longitude DataFrame
df_merged = pd.merge(c_df, df_lat_lon, on='uni', how='left')

# Save the merged DataFrame to a new CSV file
try:
    df_merged.to_csv('data/data.csv', index=False)
    print("Save success!")
except Exception as e:
    print(f"Save failed: {e}")
