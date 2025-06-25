*Find whether any of a number of date variables falls within some date range.

*1. Create test data.

set seed 1.

data list free/id.
begin data
1 2 3 4 5
end data.

do repeat x = x1 to x5.
compute x = datesum(date.dmy(1,1,2014),trunc(rv.uni(0,1000)),'days').
end repeat.
exe.

formats x1 to x5(edate10).

*2. Test data ready, actual solution starts here.

compute first_q_2014 = 0.

*Note: LOOP with VECTOR is a faster alternative for DO REPEAT below.

do repeat x = x1 to x5.
if range(x,date.dmy(1,1,2014),date.dmy(31,3,2014)) first_q_2014 = 1.
end repeat.
exe.

value labels first_q_2014 0 'None of the dates is within first quarter of 2014' 1 'At least one of the dates within first quarter 2014'.
