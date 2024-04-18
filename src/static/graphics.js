// Obtener datos para el gráfico de tipos de Pokémon desde Flask

d3.json("/data/pie-chart").then(function(data) {
    const pieData = Object.entries(data);

    const width = 300;
    const height = 200;
    const radius = Math.min(width, height) / 2;

    const color = d3.scaleOrdinal()
        .range(d3.schemeCategory10);

    const pie = d3.pie()
        .value(d => d[1])
        .sort(null);

    const arc = d3.arc()
        .innerRadius(0)
        .outerRadius(radius);

    const svg = d3.select("#pie-chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    const g = svg.selectAll(".arc")
        .data(pie(pieData))
        .enter().append("g")
        .attr("class", "arc");

    g.append("path")
        .attr("d", arc)
        .style("fill", d => color(d.data[0]));

    g.append("text")
        .attr("transform", d => "translate(" + arc.centroid(d) + ")")
        .attr("dy", ".35em")
        .text(d => d.data[0]);
});



// Obtener datos para el gráfico de línea de promedio de pesos de Pokémon desde Flask
d3.json("/data/average-weight").then(function(data) {
    // Parsear los datos y calcular el promedio de los pesos
    const pokemonData = data;
    const averageWeight = d3.mean(pokemonData, d => d.peso);

    // Crear los datos para la línea del promedio
    const lineData = [{ x: 0, y: averageWeight }, { x: pokemonData.length - 1, y: averageWeight }];

    // Configurar las dimensiones del gráfico
    const width = 300;
    const height = 200;
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    // Escala para el eje x
    const xScale = d3.scaleLinear()
        .domain([0, pokemonData.length - 1])
        .range([0, innerWidth]);

    // Escala para el eje y
    const yScale = d3.scaleLinear()
        .domain([0, d3.max(pokemonData, d => d.peso)])
        .range([innerHeight, 0]);

    // Función generadora de líneas
    const line = d3.line()
        .x((d, i) => xScale(i))
        .y(d => yScale(d.y))
        .curve(d3.curveMonotoneX);

    // Crear el contenedor SVG para el gráfico
    const svg = d3.select("#average-weight-chart").append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // Agregar la línea del promedio
    svg.append("path")
        .datum(lineData)
        .attr("class", "average-line")
        .attr("d", line);

    // Agregar los puntos de datos
    svg.selectAll(".dot")
        .data(pokemonData)
        .enter().append("circle")
        .attr("class", "dot")
        .attr("cx", (d, i) => xScale(i))
        .attr("cy", d => yScale(d.peso))
        .attr("r", 3);

    // Agregar ejes
    svg.append("g")
        .attr("class", "x-axis")
        .attr("transform", `translate(0, ${innerHeight})`)
        .call(d3.axisBottom(xScale));

    svg.append("g")
        .attr("class", "y-axis")
        .call(d3.axisLeft(yScale));

    // Agregar etiquetas
    svg.append("text")
        .attr("class", "axis-label")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (innerHeight / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Peso");

    svg.append("text")
        .attr("class", "axis-label")
        .attr("x", innerWidth / 2)
        .attr("y", innerHeight + margin.bottom)
        .style("text-anchor", "middle")
        .text("Pokémon");

    svg.append("text")
        .attr("class", "average-label")
        .attr("x", xScale(pokemonData.length - 1))
        .attr("y", yScale(averageWeight) - 10)
        .attr("dy", "0.35em")
        .text("Promedio");
});


d3.json("/data/bar-chart").then(function(data) {
    const typeData = Object.entries(data);
    const typeSvg = d3.select("#type-chart").append("svg").attr("width", 300).attr("height", 200);
    const typeBars = typeSvg.selectAll("rect").data(typeData).enter().append("rect");
    typeBars.attr("x", (d, i) => i * 50).attr("y", d => 200 - d[1] * 10).attr("width", 40).attr("height", d => d[1] * 10);
    typeBars.attr("fill", "steelblue").attr("opacity", 0.7);
    typeBars.attr("transform", "translate(10,0)");
    typeSvg.selectAll("text").data(typeData).enter().append("text").text(d => d[0]).attr("x", (d, i) => i * 50).attr("y", 190).attr("transform", "translate(30,0)");
});

// Obtener datos para el gráfico de altura de Pokémon desde Flask
d3.json("/data/scatter-plot").then(function(data) {
    const heightData = data;
    const heightSvg = d3.select("#height-chart").append("svg").attr("width", 300).attr("height", 200);
    const heightBars = heightSvg.selectAll("circle").data(heightData).enter().append("circle");
    heightBars.attr("cx", (d, i) => i * 50 + 20).attr("cy", d => 200 - d.altura * 2).attr("r", 5);
    heightBars.attr("fill", "green").attr("opacity", 0.7);
    heightBars.attr("transform", "translate(10,0)");
    heightSvg.selectAll("text").data(heightData).enter().append("text").text(d => d.nombre).attr("x", (d, i) => i * 50).attr("y", 190).attr("transform", "translate(30,0)");
});

// Obtener datos para el gráfico de línea de promedio de pesos de Pokémon desde Flask
d3.json("/data/line-chart").then(function(data) {
    const averageWeight = data.average_weight;
    const lineData = [{ x: 0, y: averageWeight }, { x: 1, y: averageWeight }];
    const margin = { top: 20, right: 20, bottom: 30, left: 50 };
    const width = 400 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    const svg = d3.select("#line-chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    const x = d3.scaleLinear().range([0, width]);
    const y = d3.scaleLinear().range([height, 0]);

    const line = d3.line()
        .x(d => x(d.x))
        .y(d => y(d.y));

    x.domain(d3.extent(lineData, d => d.x));
    y.domain([0, d3.max(lineData, d => d.y)]);

    svg.append("path")
        .data([lineData])
        .attr("class", "line")
        .attr("d", line);

    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    svg.append("g")
        .call(d3.axisLeft(y));
});

// Obtener datos para el gráfico de línea (promedio de pesos de Pokémon)
d3.json("/data/average-weight").then(function(data) {
    const averageWeight = data.average_weight;
    const lineData = [{ x: 0, y: averageWeight }, { x: 400, y: averageWeight }]; // Linea horizontal en el promedio de peso

    const lineSvg = d3.select("#line-chart").append("svg").attr("width", 500).attr("height", 300);
    const line = d3.line()
        .x(d => d.x)
        .y(d => d.y);

    lineSvg.append("path")
        .datum(lineData)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 2)
        .attr("d", line);

    lineSvg.append("text")
        .attr("x", 10)
        .attr("y", averageWeight + 20)
        .text("Promedio de Peso: " + averageWeight)
        .attr("fill", "steelblue")
        .attr("font-size", "12px");
});
