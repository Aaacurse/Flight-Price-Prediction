document.addEventListener('DOMContentLoaded', function() {
    // Set the min attribute of the date input to today's date
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('datePicker').setAttribute('min', today);
});


function populatedest() {
    var source = document.getElementById("Source").value;
    var destination = document.getElementById("Destination");

    // Clear previous options
    destination.innerHTML = '<option value="" selected disabled>Select Destination</option>';

    // Define possible destinations based on the source
    var destinations = {
        Chennai: ["Delhi", "Hyderabad", "Kolkata", "Mumbai"],
        Delhi: ["Chennai", "Hyderabad", "Kolkata", "Mumbai"],
        Hyderabad: ["Chennai", "Delhi", "Kolkata", "Mumbai"],
        Kolkata: ["Chennai", "Delhi", "Hyderabad", "Mumbai"],
        Mumbai: ["Chennai", "Delhi", "Hyderabad", "Kolkata"]
    };

    // Populate destination options
    if (destinations[source]) {
        destinations[source].forEach(function(dest) {
            var option = document.createElement("option");
            option.value = dest;
            option.text = dest;
            destination.appendChild(option);
        });
    }
}

function calculateDays() {
    const today = new Date();
    const selectedDate = new Date(document.getElementById('datePicker').value);

    if (isNaN(selectedDate.getTime())) {
        document.getElementById('daysDifference').value = "";
        return;
    }

    const timeDifference = Math.abs(selectedDate - today);
    const dayDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));

    document.getElementById('daysDifference').value = dayDifference;
}

function populatetime(){
    var deptime=document.getElementById("Departure").value;
    var arrival=document.getElementById("Arrival");

    arrival.innerHTML='<option value=""selected disabled>Select Arrival time</option>';

    var arrivals = {
        "Early Morning":["Morning","Evening","Night"],
        "Morning":["Evening","Night","Late Night"],
        "Evening":["Night","Late Night","Early Morning"],
        "Night":["Late Night","Early Morning","Morning"],
        "Late Night":["Early Morning","Morning","Evening"]
    };

    if (arrivals[deptime]) {
        arrivals[deptime].forEach(function(time) {
            var option = document.createElement("option");
            option.value = time;
            option.text = time;
            arrival.appendChild(option);
        });
    }
}