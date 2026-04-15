async function loadMembers() {
    try {
        const response = await fetch("http://localhost:9081/members");
        const members = await response.json();

        const table = document.getElementById("members-table");
        table.innerHTML = "";

        members.forEach(emp => {
            const row = `
                <tr>
                    <td>${emp.id}</td>
                    <td>${emp.first_name}</td>
                    <td>${emp.last_name}</td>
                </tr>
            `;
            table.innerHTML += row;
        });

    } catch (error) {
        console.error("Error loading members:", error);
    }
}

async function loadLocations() {
    try {
        const country = document.getElementById("country-select").value;
        const response = await fetch(`http://localhost:9080/locations?country=${country}`);
        const locations = await response.json();

        const table = document.getElementById("locations-table");
        table.innerHTML = "";

        locations.forEach(loc => {
            const row = `
                <tr>
                    <td>${loc.wlc}</td>
                    <td>${loc.campus_id}</td>
                    <td>${loc.campus_name}</td>
                </tr>
            `;
            table.innerHTML += row;
        });

    } catch (error) {
        console.error("Error loading locations:", error);
    }
}

async function loadCountries() {
    try {
        const response = await fetch("http://localhost:9080/locations/countries");
        const countries = await response.json();

        const select = document.getElementById("country-select");
        select.innerHTML =`<option value="">Select a country</option>`

        countries.forEach(country => {
            const option = `
                <option value="${country}">${country}</option>
            `;
            select.innerHTML += option;
        });

    } catch (error) {
        console.error("Error loading countries:", error);
    }
}

