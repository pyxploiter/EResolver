$(document).ready(function(){
	$.ajax({
		url: "http://localhost/foodLab/calls/getRevenue.php",
		method: "GET",
		success: function(data) {
			console.log(data);
			
			var revenue = [];
			var date = [];

			for(var i=0; i < data.length; i++) {
				console.log(data[i].date);
				 revenue.push( data[i].revenue);
				 date.push(data[i].date);
			}
			
			var chartdata = {
				labels: date,
				datasets : [
					{
						label: 'Revenue Generated',
						backgroundColor: 'rgba(200, 200, 200, 0.75)',
						borderColor: 'rgba(200, 200, 200, 0.75)',
						hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
						hoverBorderColor: 'rgba(200, 200, 200, 1)',
						data: revenue
					}
				]
			};

			var ctx = $("#mycanvas");

			var barGraph = new Chart(ctx, {
				type: 'bar',
				data: chartdata,
				options: {
			         tooltips: {
			          mode: 'label'
			      },
		      		responsive: true,
					      scales: {
					          xAxes: [{
					              ticks:{
					                  stepSize : 100,

					              },
					              stacked: true,
					            gridLines: {
					                    lineWidth: 0,
					                }
					          }],
					          yAxes: [{

					              stacked: true,
					               ticks: {
					                  min: 0,
					                  stepSize: 3000,
					              }

					          }]
					      }
		      	} 
			});
		},
		error: function(data) {
			console.log(data);
		}
	});


}


);