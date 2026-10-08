async function predict() {

    const fields = [

        "packet_rate",

        "deauth_rate",

        "failed_auth_attempts",

        "unique_source_count",

        "avg_signal_dbm",

        "connection_duration_sec",

        "retry_rate"

    ];

    const data = {};


    for (const field of fields) {

        data[field] =
            Number(
                document
                    .getElementById(field)
                    .value
            );

    }

    const result =
        document.getElementById("result");


    result.className =
        "result neutral";


    result.innerHTML =
        "🔄 Analyzing wireless traffic...";


    try {

        const response =
            await fetch(
                "/predict",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(data)

                }
            );


        const output =
            await response.json();



        if (!output.success) {

            result.className =
                "result danger";

            result.innerHTML =
                "❌ Error: " +
                output.error;

            return;

        }

        document
            .getElementById("normal")
            .textContent =
                output.normal_probability +
                "%";


        document
            .getElementById("attack")
            .textContent =
                output.attack_probability +
                "%";


        if (output.prediction === 1) {


            result.className =
                "result danger";


            result.innerHTML =

                "⚠️ <b>" +
                output.status +
                "</b><br><br>" +

                "Severity: " +
                output.severity;


        }

        else {


            result.className =
                "result safe";


            result.innerHTML =

                "✅ <b>" +
                output.status +
                "</b><br><br>" +

                "Severity: " +
                output.severity;

        }


    }

    catch (error) {


        result.className =
            "result danger";


        result.innerHTML =
            "❌ Unable to connect to the server.";


        console.error(error);

    }

}