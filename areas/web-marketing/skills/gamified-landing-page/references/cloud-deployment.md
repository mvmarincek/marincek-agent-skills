# Estratégias de publicação: local e clouds

| Ambiente | Hospedagem típica | Backend/formulário | Analytics/observabilidade |
|---|---|---|---|
| Local | Vite/Next dev + previews | mock/dev local | eventos console/development |
| Neutro | Vercel/Netlify/Render/Cloudflare Pages | API própria, functions | OTel + analytics consentido |
| AWS | S3+CloudFront para estático, Amplify, ECS/Cloud Run equivalente em AWS | Lambda/API Gateway | CloudWatch/RUM |
| GCP | Firebase Hosting, Cloud Run | Cloud Functions/Cloud Run | Cloud Logging/Monitoring |
| Azure | Static Web Apps, App Service | Azure Functions | Azure Monitor/App Insights |

Exigir aprovação antes de publicar, comprar domínio, ativar billing ou editar DNS. APIs de pagamento, autenticação e dados pessoais exigem proteção adicional e testes end-to-end.

## Performance budgets (iniciais, não garantias)
Meta aspiracional em campo para Core Web Vitals: LCP <= 2,5 s; INP <= 200 ms; CLS <= 0,1 nos percentis pertinentes. Auditar com Lighthouse e dados reais quando houver. Para landing imersiva, monitorar FPS, memória de GPU, long tasks, peso de JS e custo de 3D.
