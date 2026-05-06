// =========================
// PREDICTION
// =========================

function predictStock() {

  const symbol =
    document.getElementById(
      'stockInput'
    ).value;

  fetch(
    `http://127.0.0.1:8000/predict/${symbol}`
  )

  .then(res => res.json())

  .then(data => {

    document.getElementById(
      'predictedPrice'
    ).innerHTML =
      '$' + data.predicted_price;

    document.getElementById(
      'riskScore'
    ).innerHTML =
      data.risk_score + '/10';

    document.getElementById(
      'signalOutput'
    ).innerHTML =
      data.signal;

  });

}


// =========================
// PORTFOLIO CHART
// =========================

fetch('http://127.0.0.1:8000/portfolio')

.then(res => res.json())

.then(data => {

  const labels =
    data.map(item => item.Datetime);

  const values =
    data.map(item =>
      item.Portfolio_Value
    );

  const ctx =
    document.getElementById(
      'portfolioChart'
    );

  new Chart(ctx, {

    type: 'line',

    data: {

      labels: labels,

      datasets: [{

        label: 'Portfolio Value',

        data: values,

        borderColor: '#22d3ee',

        backgroundColor:
          'rgba(34,211,238,0.2)',

        fill: true,

        tension: 0.4,

        borderWidth: 2
      }]
    }
  });

});


// =========================
// PIE CHART
// =========================

fetch('http://127.0.0.1:8000/allocations')

.then(res => res.json())

.then(data => {

  const pieCtx =
    document.getElementById(
      'pieChart'
    );

  new Chart(pieCtx, {

    type: 'doughnut',

    data: {

      labels: [
        'Oil',
        'Gold',
        'Bonds'
      ],

      datasets: [{

        data: [

          data.oil_weight * 100,

          data.gold_weight * 100,

          data.bond_weight * 100

        ],

        backgroundColor: [

          '#ef4444',

          '#eab308',

          '#22c55e'

        ]
      }]
    }
  });

});


// =========================
// METRICS
// =========================

fetch('http://127.0.0.1:8000/metrics')

.then(res => res.json())

.then(data => {

  document.getElementById(
    'portfolioValue'
  ).innerHTML =
    '$' +
    data.final_portfolio_value;

  document.getElementById(
    'totalReturn'
  ).innerHTML =
    data.total_return + '%';

});


// =========================
// RISK
// =========================

fetch('http://127.0.0.1:8000/risk')

.then(res => res.json())

.then(data => {

  document.getElementById(
    'volatility'
  ).innerHTML =
    data.volatility;

  document.getElementById(
    'drawdown'
  ).innerHTML =
    data.max_drawdown;

});


// =========================
// SIGNALS
// =========================

fetch('http://127.0.0.1:8000/signals')

.then(res => res.json())

.then(data => {

  const table =
    document.getElementById(
      'signalsTable'
    );

  table.innerHTML = '';

  data.reverse().forEach(signal => {

    let signalText = '';

    let signalClass = '';

    if (signal.Signal === 1) {

      signalText = 'BUY';

      signalClass = 'buy';

    }

    else if (
      signal.Signal === -1
    ) {

      signalText = 'SELL';

      signalClass = 'sell';

    }

    else {

      signalText = 'HOLD';

      signalClass = 'hold';
    }

    table.innerHTML += `

      <tr>

        <td>
          ${signal.Datetime}
        </td>

        <td>
          ${parseFloat(
            signal.Close
          ).toFixed(2)}
        </td>

        <td class="${signalClass}">
          ${signalText}
        </td>

      </tr>

    `;
  });

});