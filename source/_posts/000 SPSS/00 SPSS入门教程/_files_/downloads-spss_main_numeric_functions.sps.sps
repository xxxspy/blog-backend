*Set working directory.

cd 'd:/temp'.

*Open data.

get file 'hospital.sav'.

*Specify 6 as user missing value for food_rating and facilities_rating.

missing values food_rating facilities_rating (6).

*Add food_rating and facilities_rating.

compute add_1 =  food_rating + facilities_rating.
exe.

*Subtract food_rating from facilities_rating.

compute subtract_1 =  food_rating - facilities_rating.
exe.

*Multiply food_rating with _facilities_rating.

compute multiply_1 =  food_rating * facilities_rating.
exe.

*Divide food_rating by _facilities_rating.

compute divide_1 =  food_rating / facilities_rating.
exe.

*1. Square food_rating.

compute exponentiate_1 =  food_rating **2.
exe.

*2. Compute cubic root of food_rating.

compute exponentiate_2 =  food_rating **(1/3).
exe.

*3. Raise food_rating to the power facilities_rating.

compute exponentiate_3 =  food_rating ** facilities_rating.
exe.

*Compute square root of food_rating.

compute square_root_1 = sqrt(food_rating).
exe.

*1. Round square_root_1 to nearest integer.

compute rnd_1 = rnd(square_root_1).
exe.

*2. Round square_root_1 to nearest quarter value.

compute rnd_2 = rnd(square_root_1,.25).
exe.

*3. Round square_root_1 to nearest integer.

compute rnd_3 = rnd(exponentiate_3,10).
exe.

*1. Trunc square_root_1 to nearest integer.

compute trunc_1 = trunc(square_root_1).
exe.

*2. Truncate square_root_1 to nearest quarter value.

compute trunc_2 = trunc(square_root_1,.25).
exe.

*3. Truncate square_root_1 to nearest integer.

compute trunc_3 = trunc(exponentiate_3,10).
exe.

*1. Extract the decimals of square_root_1.

compute mod_1 = mod(square_root_1,1).
exe.

*2. Remove all tenfolds of exponentiate_3.

compute mod_2 = mod(exponentiate_3,10).
exe.

