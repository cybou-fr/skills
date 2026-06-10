---
name: static-platform-deploy
description: Prepare deployment plans for static/web platforms such as Vercel, Netlify, Cloudflare Pages, Render, and similar services with environment, secrets, preview, rollback, and DNS checks.
---

# Static Platform Deploy

## Procedure

1. Identify platform and project.
2. Check build command and output directory.
3. Check environment variables.
4. Check secrets handling.
5. Use preview deploy first.
6. Check DNS/custom domain.
7. Prepare rollback plan.
8. Request approval for production deploy or DNS change.

## Safety

Never print deployment tokens or environment secrets.

## Required output

End with:
- scope;
- summary;
- artifacts produced or changed;
- checks performed;
- risks or approvals;
- next steps.

## Runtime notes

Follow CYBOU policy, tool adapters, scope objects, approval state, redaction, and audit requirements.

If the task touches production, external publishing, repository writes, credentials, customer data, or third-party services, check policy and request approval before any side effect.
