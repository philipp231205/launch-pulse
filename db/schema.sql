CREATE TABLE IF NOT EXISTS launches (
	id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	rocket text NOT NULL,
	provider text NOT NULL,
	launch_time timestamptz NOT NULL,
	status text NOT NULL DEFAULT 'upcoming' CHECK (status IN ('upcoming', 'launched', 'scrubbed', 'failed')),
	is_crewed boolean NOT NULL DEFAULT false,
	webcast_url text
);