def roi(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate):
    annual_roi=annual_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate)/improvement_cost
    total_roi=total_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate)/improvement_cost
    print('annual roi: ',int(round(annual_roi,0)),':1')
    print('total roi:', int(round(total_roi,0)),':1')
    return

def annual_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate):
    ana=total_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate)/EPL
    ana=round(ana,0)
    return ana

def total_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate):
    tot=future_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate)/((1+i)**EPL)
    tot=round(tot,0)
    return tot

def future_gain_from_improvement(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate):
    fut=(annual_site_profit*(improved_conversion_rate/current_conversion_rate))-(annual_site_profit*(((1+i)**EPL)-1))/(i-(improvement_cost*((1+i)**EPL)))
    fut=round(fut,0)
    return fut

print("Calculating ROI")
annual_site_profit=float(input('annual site profit:'))
improvement_cost=float(input('improvement cost:'))
i=float(input('interest rate(per annum):'))
EPL=float(input('Expected project life(years):'))

print('current conversion rate=visitors who purchased/site visitors')
visitors_who_purchased1=int(input('visitors who purchased:'))
site_visitors1=int(input('site visitors: '))

if visitors_who_purchased1>site_visitors1:
    print('invalid coversion rate')
    visitors_who_purchased1=int(input('visitors who purchased:'))
    site_visitors1=int(input('site visitors: '))
current_conversion_rate=(visitors_who_purchased1/site_visitors1)*100


print('improved conversion rate=visitors who purchased/site visitors')
visitors_who_purchased2=int(input('visitors who purchased:'))
site_visitors2=int(input('site visitors: '))
if visitors_who_purchased2>site_visitors2:
    print('invalid coversion rate,enter again')
    visitors_who_purchased2=int(input('visitors who purchased:'))
    site_visitors2=int(input('site visitors: '))
improved_conversion_rate=(visitors_who_purchased2/site_visitors2)*100

roi(annual_site_profit,improvement_cost,i,EPL,current_conversion_rate, improved_conversion_rate)
