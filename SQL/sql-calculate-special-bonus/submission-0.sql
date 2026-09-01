-- Write your query below

select employee_id, case 
                    when employee_id % 2 = 1 AND name NOT LIKE 'M%' then salary else 0
                    end as bonus

                    from employees ORDER BY employee_id
