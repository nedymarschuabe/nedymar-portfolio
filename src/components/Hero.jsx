import { profile } from "../data";

export default function Hero() {
  const initials = profile.name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .slice(0, 2);

  return (
    <header className="hero">
      <div className="hero__avatar" aria-hidden="true">
        {initials}
      </div>
      <h1>{profile.name}</h1>
      <p className="hero__title">{profile.title}</p>
      <p className="hero__subtitle">{profile.subtitle}</p>
      <p className="hero__location">📍 {profile.location}</p>

      <div className="hero__links">
        <a href={`mailto:${profile.email}`}>{profile.email}</a>
        <a href={`tel:+55${profile.phone.replace(/\D/g, "")}`}>{profile.phone}</a>
        <a href={profile.linkedin} target="_blank" rel="noreferrer">
          LinkedIn
        </a>
        <a href={profile.github} target="_blank" rel="noreferrer">
          GitHub
        </a>
      </div>
    </header>
  );
}
