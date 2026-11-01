/** Opt-in analytics adapter. No tracking without explicit consent and configured transport. */
export type LandingEvent =
  | 'cta_click' | 'section_view' | 'video_start' | 'video_progress'
  | 'video_complete' | 'graphic_interaction' | 'form_start'
  | 'form_error' | 'generate_lead' | 'conversion_verified' | 'experiment_exposure';
export type EventProperties = Record<string, string | number | boolean | null>;
export type SendEvent = (event: string, properties: EventProperties) => Promise<void> | void;
export class LandingAnalytics {
  constructor(private readonly hasConsent: () => boolean,
              private readonly send: SendEvent) {}
  async track(name: LandingEvent, props: EventProperties = {}): Promise<boolean> {
    if (!this.hasConsent()) return false;
    // Use an explicit allowlist instead of sending arbitrary input fields.
    const forbidden = /password|email|phone|cpf|name|address|token|secret|message|input/i;
    const safe = Object.fromEntries(Object.entries(props).filter(([k, v]) =>
      !forbidden.test(k) && (v === null || ['string', 'number', 'boolean'].includes(typeof v))));
    await this.send(name, safe);
    return true;
  }
}
