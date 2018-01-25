import os
from flask import Flask, render_template,request,jsonify,url_for
import stripe,json,requests
from flask_json import FlaskJSON, JsonError, json_response
app = Flask(__name__)

print(os.environ.get('PUB_API_KEY'))
print(os.environ.get('SEC_API_KEY'))

stripe_keys = {
  'secret_key': os.environ['SEC_API_KEY'],
  'publishable_key': os.environ['PUB_API_KEY']
}

stripe.api_key = stripe_keys['secret_key']

@app.route('/main')
def home():
		return render_template('form.html')

@app.route('/msub')
def msub():
		return render_template('multiple_subscribe.html')

@app.route('/mul',methods=['POST'])
def mul():
	cust=request.form['customer_id']
	plan= request.form.getlist('plan_id')
	print(plan)
	bill=request.form['bill']
	return 'read'
	#return render_template('mul_subscribe.html')


@app.route('/list_customer')
def list_customer():
	lcus=stripe.Customer.list(limit=4)
	return jsonify(lcus)
	
@app.route('/plan')
def list_plan():
	total=[]
	lplan=stripe.Plan.list(limit=10)	
	return jsonify(lplan)

@app.route('/cusid')
def customer_id():
	list1=stripe.Customer.list(limit=100)
	total=[]
	for i in list1:
		d={}
		d['id']=i['id']
		total.append(d)
		result=total
	return jsonify(result)

'''@app.route('/subid')
def subscription_id():
	list1=stripe.Customer.list(limit=100)
	sub=[]
	#code for accessing subscription id:
	for i in list1:
		s={}
		s["subscriptions"]=i["subscriptions"]
		sub.append(s)
		sub_result=sub
	return jsonify(sub_result)
'''


'''@app.route('/subscribe')
def sudscribe():
	list1=stripe.Customer.list(limit=100)
	total=[]
	#cusid=[]
	for i in list1:
		d={}
		d['id']=i['id']
		total.append(d)
		result=total
		print(d['id'])
	for j in result:
		d1={}
		d1['id']=j['id']
		sub=stripe.Subscription.create(
  		customer=d1['id'],
  		items=[
			{
			  "plan": "silver-complete",
			},
  		 ]
		
		)
			#cusid.append(sub)

	return jsonify(sub)
'''
#each customer can subscribe to either of many plans
@app.route('/subscribe',methods=['POST'])
def subscribe():
	cust=request.form['customer_id']
	plan= request.form['plan_id']
	bill=request.form['bill']
	try:
		if plan=="silver-complete":
			if bill=="send_invoice":
				sub=stripe.Subscription.create(
			  		customer=cust,
			  		billing=bill,
			  		days_until_due=10,
			  		items=[
						{
						  "plan": "silver-complete",
						  #"plan": "Yearly complete",
						  #"plan": "online-access",
						  #"plan": "home-delivery",
						  #"plan": "additional-license",

						},
			  		 ]
					
					)
				return '<h1><center>Plan is subscribed </center></h1>'

			elif bill=="charge_automatically":
				sub=stripe.Subscription.create(
			  		customer=cust,
			  		billing=bill,
			  		#days_until_due=none,
			  		items=[
						{
						  "plan": "silver-complete",
						  #"plan": "Yearly complete",
						  #"plan": "online-access",
						  #"plan": "home-delivery",
						  #"plan": "additional-license",

						},
			  		 ]
					
					)
				return '<h1><center>Plan is subscribed </center></h1>'
			else:
				return bill+'<h1><center>Billing type is not available</center></h1>'
		else:
			return render_template('error.html')

	except requests.exceptions.RequestException as e:
   		raise ThreatStackRequestError(e.args)

#each customer can subscribe to multiple subscription
@app.route('/multiple_subscription',methods=['POST'])
def multiple_subscribe():
	cust=request.form['customer_id']
	plan= request.form.getlist('plan_id')
	print(plan)
	bill=request.form['bill']
	i=0
	for x in plan:
		if plan[i]=='online-access':
			if bill=="send_invoice":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	days_until_due=10,
			  	tax_percent=6.34,
				items=[{'plan': 'online-access'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

			elif bill=="charge_automatically":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	#days_until_due=10,
				items=[{'plan': 'online-access'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

		elif plan[i]=='home-delivery':
			if bill=="send_invoice":
				sub2 = stripe.Subscription.create(
				  customer=cust,
				  billing=bill,
			  	  days_until_due=10,
				  items=[{'plan': 'home-delivery'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

			elif bill=="charge_automatically":
				sub2 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
				#days_until_due=10,
				items=[{'plan': 'home-delivery'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

		elif plan[i]=='silver-complete':
			if bill=="send_invoice":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	days_until_due=10,
				items=[{'plan': 'silver-complete'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

			elif bill=="charge_automatically":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	#days_until_due=10,
				items=[{'plan': 'silver-complete'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'


		elif plan[i]=='Yearly complete':
			if bill=="send_invoice":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	days_until_due=10,
				items=[{'plan': 'Yearly complete'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

			elif bill=="charge_automatically":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	#days_until_due=10,
				items=[{'plan': 'Yearly complete'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'


		elif plan[i]=='additional-license':
			if bill=="send_invoice":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	days_until_due=10,
				items=[{'plan': 'additional-license'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'

			elif bill=="charge_automatically":
				sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	#days_until_due=10,
				items=[{'plan': 'additional-license'}],
				)
				i=i+1
				return '<h1><center>Plan is subscribed </center></h1>'


		else:
			return render_template('error.html')



#each customer can subscribe to multiple plans

@app.route('/multiple_plans',methods=['POST'])
def mulplans():
	cust=request.form['customer_id']
	#plan= request.form.getlist('plan_id')
	bill=request.form['bill']

	if bill=="send_invoice":
		sub1 = stripe.Subscription.create(
				customer=cust,
				billing=bill,
			  	days_until_due=10,
				items=[
				{'plan': 'additional-license'},
				{'plan': 'silver-complete',
				  'quantity':2,
				},
				],
				)
		return '<h1><center>Plan is subscribed </center></h1>'
				
	else:
		subscription = stripe.Subscription.create(
			  customer=cust,
			  items=[
			    {
			      'plan': 'silver-complete',
			    },
			    {
			      'plan': 'additional-license',
			      'quantity': 2,
			    },
			  ],
			)
		return '<h1><center>Plan is subscribed </center></h1>'





@app.route('/listsub')
def list_subscrption():
	lsub=stripe.Subscription.list(limit=3)
	return jsonify(lsub)

		

		
	
	



if __name__ == '__main__':
	app.run(debug=True)