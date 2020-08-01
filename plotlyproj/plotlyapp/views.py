from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.utils import timezone
from .models import *
######chartit example########
from chartit import DataPool, Chart, PivotDataPool, PivotChart
######flexmonster example#########
from django.http import JsonResponse
from django.core import serializers


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = UserPlotData.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


###############################chartit##############################
# Create your views here.
def index(request):
    plotdata = \
        DataPool(
        series=
            [{'options': {
                'source': UserPlotData.objects.all()},
                'terms': [
                    'date',
                    'avgLbsPerReps'
                ]}
            ])
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = plotdata,
            series_options =
            [{'options':{
                'type': 'line',
                'stacking': False},
                'terms':{
                'date': [
                    'avgLbsPerReps']
                }}],
            chart_options =
            {'title': {
                'text': 'Pounds per week chart'},
            'xAxis': {
                    'title':{
                    'text': 'Date'}},
            'YAxis': {
                    'title': {
                    'text': 'Pounds per Reps'}}})
    #Step 2: Create the Chart object
    cht2 = Chart(
            datasource = plotdata,
            series_options =
            [{'options':{
                'type': 'pie',
                'stacking': False},
                'terms':{
                'date': [
                    'avgLbsPerReps']
                }}],
            chart_options =
            {'title': {
                'text': 'Workout Pattern - Pie chart'},
            'xAxis': {
                    'title':{
                    'text': 'Week'}},
            'YAxis': {
                    'title': {
                    'text': 'avgerage Pounds per Reps'}}})
    #Step 3: Send the chart object to the template.
    return render(request,'index.html',{'chart_list': [cht,cht2]})