import { initMercadoPago, CardPayment } from "@mercadopago/sdk-react";

initMercadoPago("TEST-a366c187-d6bb-4b76-9696-3d01d7e3b80c");


export default function App() {

return(
  <main className="max-w-lg m-auto border" >  
    <section className="p-6">   
      <h1 className="text-center text-2x1 font-bold">
        Integrando Mercado Pago
      </h1>
      {/* <Wallet
      initialization={{
        preferenceId: "1877847170-6fc62269-1337-4ff3-a691-95af421ae265",
      }}
      /> */}
 <CardPayment
          initialization={{ amount: 500 }}
          customization={{
            visual: {
              style: {
                theme: "flat",
              },
            },
            paymentMethods: {
              creditCard: "all",
              debitCard: "all",
              ticket: "all",
              bankTransfer: "all",
              onboarding_credits: "all",
              maxInstallments: 12,
            },
          }}
          onSubmit={async (param) => {
            const response = await fetch(
              "http://127.0.0.1:8000/api/v1/create-payment/",
              {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  transaction_amount: param.transaction_amount,
                  token: param.token,
                  description: "Venta de S/500",
                  installments: param.installments,
                  payment_method_id: param.payment_method_id,
                  email: param.payer.email,
                  type: param.payer.identification.type,
                  number: param.payer.identification.number,
                }),
              }
            );
            const data = await response.json();
            console.log(data);
          }}
        />
    </section>
   </main>
  );
}