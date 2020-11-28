const api_url = 'json_data/population.json';

async function getData() {
    const response = await fetch(api_url);
    const data = await response.json();
    console.log(data.aseanGb)
    const {india, asean, aseanGb, saarc} = data;

    Highcharts.chart('container-1', {
        chart: {
            type: 'column'
        },
        title: {
            text: india.gTitle
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: india.xLabels,
            title: {
                text: india.xText,
                style: {                    
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }

            }
        },
        yAxis: {
            min: 0,
            title: {
                text: india.yText,
                style: {                    
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            },
            labels: {
                overflow: 'justify'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            valueSuffix: ' millions'
        },
        credits: {
            enabled: false
        },
        series: [{
            name:"",
            data: india.data}],
    });


    Highcharts.chart('container-2', {
        chart: {
            type: 'column'
        },
        title: {
            text: asean.gTitle
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: asean.xLabels,
            title: {
                text: asean.xText,
                style: {                    
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: asean.yText,
                style: {                    
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            },
            labels: {
                overflow: 'justify'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            valueSuffix: ' millions'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name:"ASEA",
            data: asean.data}],
    });

    Highcharts.chart('container-3', {
        chart: {
            type: 'column'
        },
        title: {
            text: saarc.gTitle
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: saarc.xLabels,
            title: {
                text: saarc.xText,
                style: {                    
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: saarc.yText,
                style: {                    
                    color: '#ff7d04',
                    fontSize: '1.5em'
                }
            },
            labels: {
                overflow: 'justify'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            valueSuffix: ' millions'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name:"SAARC",
            data: saarc.data}],
    });

    Highcharts.chart('container-4', {
        chart: {
            type: 'column'
        },
        title: {
            text: aseanGb.gTitle
        },
        subtitle: {
            text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">Population Data</a>'
        },
        xAxis: {
            categories: aseanGb.xLabels,
            title: {
                text: aseanGb.xText,
                style: {                    
                    color: '#000',
                    fontSize: '1.5em'
                }
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Population (millions)',
                style: {                    
                    color: '#000',
                    fontSize: '1.5em'
                }
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' millions'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: aseanGb.data
    });
}

getData();
