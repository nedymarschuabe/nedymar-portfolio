import { experiences } from "../data";

export default function Experience() {
  return (
    <section className="section" id="experience">
      <h2>Experiência</h2>
      <ol className="timeline">
        {experiences.map((job) => (
          <li className="timeline__item" key={`${job.company}-${job.period}`}>
            <div className="timeline__dot" aria-hidden="true" />
            <div className="timeline__content">
              <h3>{job.role}</h3>
              <p className="timeline__meta">
                {job.company} · {job.period}
              </p>
              <p className="timeline__meta timeline__meta--location">{job.location}</p>
              <p className="timeline__description">{job.description}</p>
              <ul>
                {job.bullets.map((bullet) => (
                  <li key={bullet}>{bullet}</li>
                ))}
              </ul>
            </div>
          </li>
        ))}
      </ol>
    </section>
  );
}
