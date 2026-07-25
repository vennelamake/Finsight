console.log("reports.js loaded");

document.addEventListener("DOMContentLoaded", function () {

    const period = document.getElementById("reportPeriod");
    const customRange = document.getElementById("customRange");
    const generateBtn = document.getElementById("generateReport");

    if (period && customRange) {
        period.addEventListener("change", function () {

            if (this.value === "custom") {
                customRange.style.display = "flex";
            } else {
                customRange.style.display = "none";
            }

        });
    }

    if (generateBtn) {
        generateBtn.addEventListener("click", function () {

            const selectedPeriod = period.value;

            if (selectedPeriod === "custom") {

                const from = document.getElementById("fromDate").value;
                const to = document.getElementById("toDate").value;

                if (!from || !to) {
                    alert("Please select both From and To dates.");
                    return;
                }

                window.location.href =
                    `/reports/preview?period=custom&from=${from}&to=${to}`;

            } else {

                window.location.href =
                    `/reports/preview?period=${selectedPeriod}`;

            }

        });
    }

});