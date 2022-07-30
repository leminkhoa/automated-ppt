gold_price_l14d_query = '''
with raw_data as (
SELECT 
	gold_code,
	buying_price / 1000 as buying_price,
	selling_price / 1000 as selling_price,
	last_update,
	to_char(last_update, 'YYYY-MM-DD') as date,
	dense_rank() over (partition by gold_code, to_char(last_update, 'YYYY-MM-DD') order by last_update ASC) as rank_asc,
	dense_rank() over (partition by gold_code, to_char(last_update, 'YYYY-MM-DD') order by last_update DESC) as rank_desc
	
FROM dev.get_gold_2022
where last_update >= current_date - interval '14 days' and last_update < current_date
),
avg_agg as (

select 
	gold_code,
	date,
	case when avg(buying_price) = 0 then null else round(avg(buying_price), 0) end as avg_buying_price,
	case when avg(selling_price) = 0 then null else round(avg(selling_price), 0) end as avg_selling_price
from raw_data
group by
	gold_code,
	date
order by gold_code, date
)

select 
	a.*,
	case when r_a.buying_price = 0 then null else r_a.buying_price end as first_buying_price,
	case when r_d.buying_price = 0 then null else r_d.buying_price end as last_buying_price,
	case when r_a.selling_price = 0 then null else r_a.selling_price end as fist_selling_price,
	case when r_d.selling_price = 0 then null else r_d.selling_price end as last_selling_price
from avg_agg a
left join raw_data r_a
	on 1=1
	and a.gold_code = r_a.gold_code
	and a.date = r_a.date
	and r_a.rank_asc = 1
left join raw_data r_d
	on 1=1
	and a.gold_code = r_d.gold_code
	and a.date = r_d.date
	and r_d.rank_desc = 1	
'''